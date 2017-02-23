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
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(app.config['USERNAME'])
    print(app.config['PASSWORD'])
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            return redirect(url_for('show_admin_menu'))

    return render_template('login.html', error=error)


@app.route('/admin-login/', methods=["GET"])
def check_login():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return redirect(url_for('show_admin_menu'))


@app.route('/admin/', methods=["GET"])
def show_admin_menu():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template("admin_interface.html")


@app.route('/admin/list_applicants')
def list_applicants(applicants=None):
    if not session.get('logged_in'):
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
    if not session.get('logged_in'):
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
    return render_template('mentor_interface.html')


@app.route('/mentor/interviews-list', methods=["GET"])
def show_mentor_interviews():
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


@app.route("/admin/e-mail-log", methods=["GET"])
def show_sent_email():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        emails_list = EmailDetails.select().order_by(EmailDetails.date)
        return render_template('show_email.html', header="List of all emails", emails=emails_list)


@app.route('/applicant', methods=["GET"])
def show_applicants_interface():
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

  
@app.route("/admin/filter_applicants", methods=["GET", "POST"])
def filter():
    if not session.get('logged_in'):
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


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

