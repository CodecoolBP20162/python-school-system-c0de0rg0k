from models import *


def applicants_status(app_code):
    applicant = Applicant.select().where(Applicant.applicant_code == app_code).get()
    return applicant.status
