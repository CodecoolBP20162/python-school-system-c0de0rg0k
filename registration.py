from models import *


class Register:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.applicant_city = ""
        self.status = "new"
        self.school_id = ""

    def register_applicant(self):
        self.__input_applicant_data()

    def register_mentor(self):
        self.__input_mentor_data()

    def __input_applicant_data(self):
        self.first_name = input("Tell me your first name: ")
        self.last_name = input("Tell me your last name: ")
        self.applicant_city = input("Where do you live: ")
        Applicant.create(first_name=self.first_name, last_name=self.last_name, applicant_city=self.applicant_city, status=self.status)

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
            ("There is no Codecool school at", self.school_id)