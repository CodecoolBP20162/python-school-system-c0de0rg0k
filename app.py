import os
from peewee import *
from models import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from generator.app_code_generator import AppCodeGenerator
from generator.applicant_generator import ApplicantGenerator


app = Flask(__name__)  # create the application instance :)
app.debug = True


def init_db():
    db.connect()


@app.route('/')
def index():
    return render_template('index_temp.html')



@app.route('/admin/list_applicants')
def list_applicants():
    applicants = Applicant.select().order_by(Applicant.id)
    cities = Applicant.select(fn.Distinct(Applicant.applicant_city)).order_by(Applicant.applicant_city)
    schools = Applicant.select(fn.Distinct(Applicant.applied_school)).join(School) # .order_by(Applicant.applied_school.city)
    return render_template('applicants.html',
                           applicants=applicants,
                           cities=cities,
                           schools=schools)


@app.route('/registration', methods=['GET'])
def show_registration_form():
    return render_template('applicant_registration.html')


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


if __name__ == '__main__':
    init_db
    app.run()