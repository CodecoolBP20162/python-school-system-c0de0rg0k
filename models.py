from peewee import *
from set_connection import SetConnection

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop

connected = SetConnection

db = PostgresqlDatabase(connected.username, user=connected.username)


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db


class School(BaseModel):
    city = CharField()


class Applicant(BaseModel):
    first_name = CharField()
    last_name = CharField()
    applicant_city = ForeignKeyField(City, related='city_name')
    applicant_code = CharField()
    applied_school = ForeignKeyField(School, related_name='id')
    status = CharField()


class City(BaseModel):
    city_name = PrimaryKeyField()
    nearest_school = ForeignKeyField(School, related='id')


class Mentor(BaseModel):
    first_name = CharField()
    last_name = CharField()
    school = ForeignKeyField(School, related='id')


class InterviewSlot(BaseModel):
    start_time = DateField()
    end_time = DateField()
    reserved = CharField()
    mentor = ForeignKeyField(Mentor, related='id')


class Interview(BaseModel):
    slot_id = ForeignKeyField(InterviewSlot, related='id')
    applicant_code = ForeignKeyField(Applicant, related='applicant_code')



