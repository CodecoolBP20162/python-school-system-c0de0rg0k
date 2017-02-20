from generator.app_code_generator import AppCodeGenerator
from generator.applicant_generator import ApplicantGenerator
from models import *
from registration.email_for_new_users import SendEmail


class Register:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.applicant_city = ""
        self.status = "new"
        self.school_id = ""
        self.app_code = AppCodeGenerator().code_generator()
        self.nearest_school = ""
        self.applied_school = ""

    def register_applicant(self):
        self.__input_applicant_data()

    def register_mentor(self):
        self.__input_mentor_data()

    def __input_applicant_data(self):
        self.first_name = input("Tell me your first name: ")
        self.last_name = input("Tell me your last name: ")
        self.applicant_city = input("Where do you live: ")
        self.applied_school = ApplicantGenerator().search_nearest_school(self.applicant_city)
        try:
            new_applicant = Applicant.create(first_name=self.first_name, last_name=self.last_name,
                                            applicant_city=self.applicant_city, applicant_code=self.app_code,
                                            applied_school= self.applied_school, status=self.status)
            new_applicant.save()
            SendEmail().send_email(new_applicant)
            print("Registration was successful. E-mail was sent!")
        except:
            print("Something went wrong. Registration failed")

    def __input_mentor_data(self):
        self.first_name = input("Tell me your first name: ")
        self.last_name = input("Tell me your last name: ")
        self.school_id = input("Which school would you like to attend (Budapest, Miskolc or Krakow): ")
        if self.school_id == "Budapest":
            self.school_id = "1"
            Mentor.create(first_name=self.first_name, last_name=self.last_name, school=self.school_id)
        elif self.school_id == "Miskolc":
            self.school_id = "2"
            Mentor.create(first_name=self.first_name, last_name=self.last_name, school=self.school_id)
        elif self.school_id == "Krakow":
            self.school_id = "3"
            Mentor.create(first_name=self.first_name, last_name=self.last_name, school=self.school_id)
        else:
            print("There is no Codecool school at", self.school_id)
