import os
from peewee import *
from models import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from generator.app_code_generator import AppCodeGenerator
from generator.applicant_generator import ApplicantGenerator
from filter_applicants import *



app = Flask(__name__)  # create the application instance :)


def init_db():
    db.connect()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin/')
def show_admin_menu():
    return redirect(url_for('index'))


@app.route('/admin/list_applicants')
def list_applicants(applicants=None):
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


@app.route('/registration', methods=['GET'])
def show_registration_form():
    return render_template('applicant_registration.html')


@app.route('/admin/list_interviews')
def list_interviews():
    interviews= Interview.select().join(InterviewSlot).join(Mentor)
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

@app.route('/registration', methods=['POST'])
def applicant_registration():
    Applicant.create(first_name=request.form['first_name'],
                     last_name=request.form['last_name'],
                     applicant_city=request.form['applicant_city'],
                     status="new",
                     applied_school = ApplicantGenerator().search_nearest_school(request.form['applicant_city']),
                     applicant_code= AppCodeGenerator().code_generator(),
                     email=request.form['email_address'])
    return redirect(url_for('index'))


@app.route("/admin/e-mail-log", methods=["GET"])
def show_sent_email():
    emails_list = EmailDetails.select().order_by(EmailDetails.date)
    return render_template('show_email.html', header="List of all emails", emails=emails_list)


@app.route("/admin/filter_applicants", methods=["GET", "POST"])
def filter():
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

