from models import *
from datetime import datetime


class AdministratorQueries:

    def filter_by_school(self):
        school_id = self.__input_id("school id")
        self.__check_school_id(school_id)
        self.__print_interview_by_school_id(school_id)

    def filter_by_applicant_code(self):
        applicant_code = self.__input_id("application code")
        self.__check_applicant_code(applicant_code)
        self.__print_interview_by_app_code(applicant_code)

    def filter_by_mentor_code(self):
        mentor_id = self.__input_id("mentor id")
        self.__check_mentor_id(mentor_id)
        self.__print_interview_by_mentor_id(mentor_id)

    def filter_by_date(self):
        date_from = self.__input_datetime()
        date_to = self.__input_datetime()
        self.__print_interview_by_date(date_from, date_to)

    def __input_id(self, id_type):
        id_ = input("Please add me the {0}: ".format(id_type))
        return id_

    def __input_datetime(self):
        y = int(input("Please add a year: "))
        m = int(input("Please add a month: "))
        d = int(input("Please add a day: "))
        return datetime(y, m, d)

    def __print_interview_by_school_id(self, school_id):
        interview_slot = InterviewSlot.select()
        for slot in interview_slot:
            if int(school_id) == slot.mentor.school.id:
                print(slot.mentor.school.city, slot.start_time, slot.end_time, slot.reserved, slot.mentor.last_name)

    def __print_interview_by_app_code(self, applicant_code):
        interview_slot = InterviewSlot.select()
        for slot in interview_slot:
            for interview in slot.interviews:
                if str(applicant_code) == interview.applicant_code.applicant_code:
                    print("Applicant: {0} {1} --> start time: {2}".format(interview.applicant_code.first_name, interview.applicant_code.last_name,
                                                                          slot.start_time))

    def __print_interview_by_mentor_id(self, mentor_id):
        mentors = Mentor.select()
        for mentor in mentors:
            for int_slot in mentor.interview_slots:
                if int(mentor_id) == int_slot.mentor.id:
                    print("Mentor: {0} --> {1}".format(int_slot.mentor.last_name, int_slot.start_time))

    def __print_interview_by_date(self, date_from, date_to):
        interviews_slot = InterviewSlot.select()
        for slot in interviews_slot:
            if slot.start_time > date_from and slot.end_time < date_to:
                print("Mentor: {0}: {1} --> {2}".format(slot.mentor.last_name, slot.start_time, slot.end_time))

    def __check_school_id(self, school_id):
        schools = School.select().where(School.id == school_id)
        if len(schools) == 0:
            raise ValueError

    def __check_applicant_code(self, applicant_code):
        applicants = Applicant.select().where(int(applicant_code) == Applicant.applicant_code)
        if len(applicants) == 0:
            raise ValueError

    def __check_mentor_id(self, mentor_id):
        mentors = Mentor.select().where(mentor_id == Mentor.id)
        if len(mentors) == 0:
            raise ValueError
