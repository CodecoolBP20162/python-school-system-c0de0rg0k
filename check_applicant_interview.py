from models import *

def applicant_without_interview_date():
    applicant = Applicant.select().where(Applicant.status == "new")
    return applicant