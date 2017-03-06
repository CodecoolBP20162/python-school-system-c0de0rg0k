from generator.app_code_generator import AppCodeGenerator
from generator.applicant_generator import ApplicantGenerator
from models import *
from registration.email_for_new_users import SendEmail
from unidecode import unidecode

class Register:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.applicant_city = ""
        self.status = "new"
        self.school_id = ""
        self.app_code = ""
        self.nearest_school = ""
        self.applied_school = ""
        self.email = ""
        self.password = ""

    def register_applicant(self):
        self.__input_applicant_data()
        self.app_code = AppCodeGenerator().code_generator()
        try:
            applicant_full_name = unidecode(self.first_name) + unidecode(self.last_name)
            new_applicant = Applicant.create(first_name=self.first_name, last_name=self.last_name,
                                            applicant_city=self.applicant_city, applicant_code=self.app_code,
                                            applied_school= self.applied_school, status=self.status,
                                             email='tesztfiok.codeorgok+{0}@gmail.com'.format(applicant_full_name))
            new_applicant.save()
            SendEmail().send_applicant_email(new_applicant)
            print("Registration was successful. E-mail was sent!")
        except:
            print("Something went wrong. Registration failed")

    def register_mentor(self):
        self.__input_mentor_data()
        mentor_full_name = unidecode(self.first_name) + unidecode(self.last_name)
        if self.school_id == "Budapest":
            self.school_id = "1"
            new_mentor = Mentor.create(first_name=self.first_name, last_name=self.last_name, school=self.school_id,
                                       email='tesztfiok.codeorgok+{0}@gmail.com'.format(mentor_full_name),
                                       password=self.password)
            new_mentor.save()
            SendEmail().send_mentor_email(new_mentor)
            print("Registration was successful. E-mail was sent!")
        elif self.school_id == "Miskolc":
            self.school_id = "2"
            new_mentor = Mentor.create(first_name=self.first_name, last_name=self.last_name, school=self.school_id,
                                       email='tesztfiok.codeorgok+{0}@gmail.com'.format(mentor_full_name),
                                       password=self.password)
            new_mentor.save()
            SendEmail().send_mentor_email(new_mentor)
            print("Registration was successful. E-mail was sent!")
        elif self.school_id == "Krakow":
            self.school_id = "3"
            new_mentor = Mentor.create(first_name=self.first_name, last_name=self.last_name, school=self.school_id,
                                       email='tesztfiok.codeorgok+{0}@gmail.com'.format(mentor_full_name),
                                       password=self.password)
            new_mentor.save()
            SendEmail().send_mentor_email(new_mentor)
            print("Registration was successful. E-mail was sent!")
        else:
            print("There is no Codecool school at", self.school_id)

    def __input_applicant_data(self):
        self.first_name = input("Tell me your first name: ")
        self.last_name = input("Tell me your last name: ")
        self.applicant_city = input("Where do you live: ")
        self.applied_school = ApplicantGenerator().search_nearest_school(self.applicant_city)


    def __input_mentor_data(self):
        self.first_name = input("Tell me your first name: ")
        self.last_name = input("Tell me your last name: ")
        self.school_id = input("Which school would you like to attend (Budapest, Miskolc or Krakow): ")
        self.password = input("Please choose a password: ")