from models import *
from generator.app_code_generator import AppCodeGenerator
from generator.applicant_generator import ApplicantGenerator


class NewApplicantCode:

    def __init__(self):
        self.app_code_generator = AppCodeGenerator()
        self.generate_nearest_school_id = ApplicantGenerator()
        self.__generate_appcode_and_school_id()

    def __generate_appcode_and_school_id(self):
        applicants = Applicant.select().where(Applicant.applicant_code.is_null(True))
        for app in applicants:
            new_code = self.app_code_generator
            app.applicant_code = new_code.application_code
            app.save()
        self.generate_nearest_school_id.generate_nearest_school()