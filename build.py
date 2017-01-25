# This script can create the database tables based on your models

from models import *

try:
    db.connect()
except:
    print('I can\'t connect to the database')

if School.table_exists():
    School.drop_table()

if Applicant.table_exists():
    Applicant.drop_table()

if City.table_exists():
    City.drop_table()

if Mentor.table_exists():
    Mentor.drop_table()

if InterviewSlot.table_exists():
    InterviewSlot.drop_table()

if Interview.table_exists():
    Interview.drop_table()

db.create_tables([School, Applicant, City, Mentor, InterviewSlot, Interview], safe=True)