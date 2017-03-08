import os
from peewee import *
from models import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, session
from generator.app_code_generator import AppCodeGenerator
from generator.applicant_generator import ApplicantGenerator
from filter_applicants import *
from registration.email_for_new_users import SendEmail
from validate_email import validate_email


app = Flask(__name__)
app.config.from_object(__name__)  # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'school_system.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))


def init_db():
    db.connect()


@app.route('/')
def index():
    return render_template('homepage_home.html')


@app.route('/about-the-training')
def about_training():
    return render_template("homepage_about_training.html")


@app.route('/principles')
def principles():
    return render_template("homepage_principles.html")


@app.route('/about-us')
def about_us():
    return render_template("homepage_about_us.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id'):
        error = "You are already logged in as applicant. Please log out first"
        return render_template('already_logged_in.html', error=error)
    elif session.get('mentor_logged_in'):
        error = "You are already logged in as mentor. Please log out first"
        return render_template('already_logged_in.html', error=error)
    elif session.get('admin_logged_in'):
        return redirect(url_for('show_admin_menu'))
    else:
        print(app.config['USERNAME'])
        print(app.config['PASSWORD'])
        error = None
        if request.method == 'POST':
            if request.form['username'] != app.config['USERNAME']:
                error = 'Invalid username'
            elif request.form['password'] != app.config['PASSWORD']:
                error = 'Invalid password'
            else:
                session['admin_logged_in'] = True
                return redirect(url_for('show_admin_menu'))

        return render_template('login.html', error=error)


@app.route('/admin-login/', methods=["GET"])
def check_login():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    else:
        return redirect(url_for('show_admin_menu'))


@app.route('/admin/', methods=["GET"])
def show_admin_menu():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template("admin_interface.html")


@app.route('/admin/list_applicants')
def list_applicants(applicants=None):
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    if applicants is None:
        applicants = Applicant.select().order_by(Applicant.first_name)
    else:
        applicants = applicants
    cities = Applicant.select(fn.Distinct(Applicant.applicant_city)).order_by(Applicant.applicant_city)
    schools = Applicant.select(fn.Distinct(Applicant.applied_school)).order_by(Applicant.applied_school)
    statuses = Applicant.select(fn.Distinct(Applicant.status)).order_by(Applicant.status)
    return render_template('applicants.html',
                           applicants=applicants,
                           cities=cities,
                           schools=schools,
                           statuses=statuses)


@app.route('/admin/list_interviews')
def list_interviews():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    else:
        interviews = Interview.select().join(InterviewSlot).join(Mentor)
        dates = InterviewSlot.select(fn.Distinct(InterviewSlot.start_time))
        applicant_codes = Applicant.select(fn.Distinct(Applicant.applicant_code)).order_by(Applicant.applicant_code)
        mentors = Mentor.select(fn.Distinct(Mentor.last_name)).join(InterviewSlot).join(Interview)
        schools = School.select(fn.Distinct(School.city)) # .order_by(Applicant.applied_school.city)
        return render_template('interviews.html',
                               interviews=interviews,
                               dates=dates,
                               applicant_codes=applicant_codes,
                               mentors=mentors,
                               schools=schools)


@app.route('/mentor', methods=["GET"])
def show_mentor_menu():
    return render_template('mentors_home.html')


@app.route('/mentor/interviews-list', methods=["GET"])
def show_mentor_interviews():
    if not session.get('mentor_logged_in'):
        return redirect(url_for('mentor_login'))
    else:
        slots = InterviewSlot.select().order_by(InterviewSlot.id)
        interviews_list = []
        for slot in slots:
            for interview in Interview.select():
                if interview.slot_id == slot:
                    interviews_list.append([str(slot.start_time), slot.mentor.last_name,
                                            interview.applicant_code.first_name + ' ' + interview.applicant_code.last_name, interview.applicant_code.applicant_code])

        return render_template('mentors_interviews.html', header="Mentor's interviews", interviews=interviews_list)


@app.route('/registration', methods=['GET'])
def show_registration_form():
    message = ""
    first_name = ""
    last_name = ""
    applicant_city = ""
    email_address = ""
    return render_template('applicant_registration.html', message = message, first_name=first_name, last_name=last_name,
                           applicant_city=applicant_city, email_address=email_address)


@app.route('/registration', methods=['POST'])
def applicant_registration():
    is_valid_email = validate_email(request.form['email_address'])
    if request.form['first_name'] != "" and request.form['last_name'] != "" and \
                    request.form['applicant_city'] != "" and request.form['email_address'] != "":
        if is_valid_email:
            new_applicant = Applicant.create(first_name=request.form['first_name'],
                             last_name=request.form['last_name'],
                             applicant_city=request.form['applicant_city'],
                             status="new",
                             applied_school = ApplicantGenerator().search_nearest_school(request.form['applicant_city']),
                             applicant_code= AppCodeGenerator().code_generator(),
                             email=request.form['email_address'])
            SendEmail().send_applicant_email(new_applicant)
            return redirect(url_for('index'))
        else:
            message = "E-mail address is not valid! Please add a valid e-mail!"
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            applicant_city = request.form['applicant_city']
            email_address = request.form['email_address']
            return render_template('applicant_registration.html', message=message, first_name=first_name, last_name=last_name,
                                   applicant_city=applicant_city, email_address=email_address)
    else:
        message = "All fields are required to fill!"
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        applicant_city = request.form['applicant_city']
        email_address = request.form['email_address']
        return render_template('applicant_registration.html', message=message, first_name=first_name, last_name=last_name,
                                applicant_city=applicant_city, email_address=email_address)


@app.route("/admin/e-mail-log", methods=["GET"])
def show_sent_email():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    else:
        emails_list = EmailDetails.select().order_by(EmailDetails.date)
        return render_template('show_email.html', header="List of all emails", emails=emails_list)


@app.route('/applicant', methods=["GET"])
def show_applicants_interface():
    return render_template('applicant_interface.html')


@app.route('/applicant/profile')
def profile():
    user = Applicant.select().where(Applicant.id == session['user_id']).get()
    return render_template('profile.html', user=user)


@app.route('/applicant/interview')
def interview():
    user = Applicant.select().where(Applicant.id == session['user_id']).get()
    return render_template('app_interview.html', user=user)


@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('login'))

  
@app.route("/admin/filter_applicants", methods=["GET", "POST"])
def filter():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    else:
        default_email = "tesztfiok.codeorgok+<username>@gmail.com"
        if request.form['filter_input_name']:
            return list_applicants(Filter_applicants.filter_applicants_name())
        elif request.form['filter_input_email'] != default_email:
            return list_applicants(Filter_applicants.filter_applicants_email())
        elif request.form['filter_input_city'] != "All":
            return list_applicants(Filter_applicants.filter_applicants_city())
        elif request.form['filter_input_school'] != "All":
            return list_applicants(Filter_applicants.filter_applicants_school())
        elif request.form['filter_input_status'] != "All":
            return list_applicants(Filter_applicants.filter_applicants_status())
        else:
            return list_applicants()


@app.route("/applicant/login/", methods=["GET"])
def applicant_login():
    if session.get('admin_logged_in'):
        error = "You are already logged in as admin. Please log out first"
        return render_template('already_logged_in.html', error=error)
    elif session.get('mentor_logged_in'):
        error = "You are already logged in as mentor. Please log out first"
        return render_template('already_logged_in.html', error=error)
    elif session.get('user_id'):
        return redirect(url_for('profile'))
    else:
        error = ""
        return render_template('applicant_login.html', error=error)


@app.route("/applicant/login/", methods=["POST"])
def validate_applicant():
    applicant_email = request.form['email']
    application_code = request.form['applicant_code']
    try:
        user = Applicant.select().where(Applicant.applicant_code== application_code, Applicant.email == applicant_email).get()
    except:
        error = "Wrong email or applicant code"
        return render_template('applicant_login.html', error=error)
    session['user_id'] = user.id
    return applicant_login()


@app.route('/applicant/logout/')
def applicant_logout():
    session.pop('user_id', None)
    return redirect(url_for('applicant_login'))


@app.route("/mentor/login/", methods=["GET"])
def mentor_login():
    if session.get('admin_logged_in'):
        error = "You are already logged in as admin. Please log out first"
        return render_template('already_logged_in.html', error=error)
    elif session.get('user_id'):
        error = "You are already logged in as applicant. Please log out first"
        return render_template('already_logged_in.html', error=error)
    elif session.get('mentor_logged_in'):
        return render_template('mentor_interface.html')
    else:
        error = ""
        return render_template('mentor_login.html', error=error)


@app.route("/mentor/login/", methods=["POST"])
def validate_mentor():
    mentor_email = request.form['email']
    mentor_password = request.form['password']
    try:
        mentor = Mentor.select().where(Mentor.email== mentor_email, Mentor.password == mentor_password).get()
    except:
        error = "Wrong email or password"
        return render_template('mentor_login.html', error=error)
    session['mentor_logged_in'] = True
    return redirect(url_for('mentor_login'))


@app.route('/mentor/logout/')
def mentor_logout():
    session.pop('mentor_logged_in', None)
    return redirect(url_for('mentor_login'))



if __name__ == '__main__':
    init_db()
    app.run(debug=True)

