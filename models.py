from peewee import *

from generator.set_connection import SetConnection

# Configure your database connection here
connected = SetConnection()
db = PostgresqlDatabase(database=connected.dbname, user=connected.username)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class School(BaseModel):
    city = CharField()


class City(BaseModel):
    city_name = CharField()
    nearest_school = ForeignKeyField(School, related_name='cities')


class Applicant(BaseModel):
    first_name = CharField()
    last_name = CharField()
    applicant_city = CharField()
    applicant_code = CharField(null=True)
    applied_school = ForeignKeyField(School, null=True, related_name='applicants')
    status = CharField(null=True)
    email = CharField()


class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, related_name='mentors')
    email = CharField()


class InterviewSlot(BaseModel):
    start_time = DateTimeField()
    end_time = DateTimeField()
    reserved = BooleanField()
    mentor = ForeignKeyField(Mentor, related_name='interview_slots')


class Interview(BaseModel):
    slot_id = ForeignKeyField(InterviewSlot, null=True, related_name='interviews')
    applicant_code = ForeignKeyField(Applicant, related_name='applicants_interviews')


class Q_A(BaseModel):
    applicant = ForeignKeyField(Applicant, related_name='my_questions')
    question = CharField()
    answer = CharField(null=True)
    answered = BooleanField()
    timestamp = DateTimeField()


class EmailDetails(BaseModel):
    subject = CharField()
    message = TextField()
    date = DateTimeField()
    email_type = CharField()
    person = CharField()
    email_address = CharField()




