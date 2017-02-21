import os
from peewee import *
from models import *
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash


app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , flaskr.py


def init_db():
    db.connect()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin/list_applicants')
def list_applicants():
    applicants = Applicant.select().order_by(Applicant.id)
    return render_template('applicants.html', applicants=applicants)


@app.route("/admin/e-mail-log", methods=["GET"])
def show_sent_email():
    applicant = Applicant.select()
    return render_template('show_email.html', header="List of all emails", object=applicant)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)