import os
from peewee import *
from models import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , flaskr.py
app.debug = True

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'School_system.db'),
    SECRET_KEY='development key',
    USERNAME='postgres',
    PASSWORD='asdfg'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def init_db():
    db.connect()


@app.route('/')
def index():
    return render_template('index_temp.html')



@app.route('/admin/list_applicants')
def list_applicants():
    applicants = Applicant.select().order_by(Applicant.id)
    return render_template('applicants.html', applicants=applicants)


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


if __name__ == '__main__':
    init_db()
    app.run()