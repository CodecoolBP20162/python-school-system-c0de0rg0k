import os
from peewee import *
from models import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


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
def list_applicants():
    applicants = Applicant.select().order_by(Applicant.id)
    cities = Applicant.select(fn.Distinct(Applicant.applicant_city)).order_by(Applicant.applicant_city)
    schools = Applicant.select(fn.Distinct(Applicant.applied_school)).order_by(Applicant.applied_school)
    statuses = Applicant.select(fn.Distinct(Applicant.status)).order_by(Applicant.status)
    return render_template('applicants.html',
                           applicants=applicants,
                           cities=cities,
                           schools=schools,
                           statuses=statuses)


@app.route("/admin/e-mail-log", methods=["GET"])
def show_sent_email():
    emails_list = EmailDetails.select().order_by(EmailDetails.date)
    return render_template('show_email.html', header="List of all emails", emails=emails_list)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

