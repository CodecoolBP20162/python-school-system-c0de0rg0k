from models import *


class ApplicantQueries():

    def __init__(self):
        self.applicant_code = ""

    def interview_details(self):
        self.__check_app_code()
        self.__print_interview_details()

    def status_details(self):
        self.__check_app_code()
        self.__print_status_details()

    def school_details(self):
        self.__check_app_code()
        self.__print_schools_details()

    def __check_app_code(self):
        app_code = input("Please tell me your application code: ")
        applicant = Applicant.select().where(Applicant.applicant_code==app_code).get()
        if applicant.applicant_code == "":
            raise ValueError
        else:
            self.applicant_code = applicant.applicant_code

    def __print_interview_details(self):
        applicant = Applicant.select(Applicant, Interview).join(Interview).where(Applicant.applicant_code==self.applicant_code)
        for app in applicant:
            for interview in app.applicants_interviews:
                print("Your interview date is", interview.slot_id.start_time, "at Codecool", \
                      interview.slot_id.mentor.school.city, "with", interview.slot_id.mentor.first_name, \
                      interview.slot_id.mentor.last_name)

    def __print_status_details(self):
        applicant = Applicant.select().where(Applicant.applicant_code==self.applicant_code).get()
        print("Your status is", applicant.status)

    def __print_schools_details(self):
        applicant = Applicant.select().where(Applicant.applicant_code == self.applicant_code)
        for app in applicant:
            print("Your applied school is", app.applied_school.city)