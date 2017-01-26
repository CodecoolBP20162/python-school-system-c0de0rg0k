from peewee import *
from set_connection import SetConnection

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop

connected = SetConnection()

db = PostgresqlDatabase(connected.username, user=connected.username)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class School(BaseModel):
    city = CharField()


class City(BaseModel):
    city_name = CharField()
    nearest_school = ForeignKeyField(School, related_name='city_school_cities')


class Applicant(BaseModel):
    first_name = CharField()
    last_name = CharField()
    applicant_city = CharField()
    applicant_code = CharField(null=True)
    applied_school = ForeignKeyField(School, null=True, related_name='school_ids')
    status = CharField(null=True)


class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, related_name='mentor_school_city')


class InterviewSlot(BaseModel):
    start_time = DateField()
    end_time = DateField()
    reserved = CharField()
    mentor = ForeignKeyField(Mentor, related_name='interviewslot_mentor_id')


class Interview(BaseModel):
    slot_id = ForeignKeyField(InterviewSlot, related_name='interview_interviewslot_id')
    applicant_code = ForeignKeyField(Applicant, related_name='interview_applicant_code')
