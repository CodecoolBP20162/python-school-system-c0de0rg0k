# This script can create the database tables based on your models

from models import *

try:
    db.connect()
except:
    print('I can\'t connect to the database')

if School.table_exists():
    School.drop_table(cascade=True)

if Applicant.table_exists():
    Applicant.drop_table(cascade=True)

if City.table_exists():
    City.drop_table(cascade=True)

if Mentor.table_exists():
    Mentor.drop_table(cascade=True)

if InterviewSlot.table_exists():
    InterviewSlot.drop_table(cascade=True)

if Interview.table_exists():
    Interview.drop_table(cascade=True)

db.create_tables([School, Applicant, City, Mentor, InterviewSlot, Interview], safe=True)