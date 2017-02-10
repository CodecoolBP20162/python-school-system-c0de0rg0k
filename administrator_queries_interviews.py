from models import *
from datetime import datetime


class AdministratorQueriesInterviews:

    def filter_by_school(self):
        school_id = self.__input_id("school id")
        self.__check_school_id(school_id)
        interview_list = self.__select_interview_by_school(school_id)
        max_length = self.__search_longest_element(interview_list)
        self.__print_interview(interview_list, max_length)

    def filter_by_applicant_code(self):
        applicant_code = self.__input_id("application code")
        self.__check_applicant_code(applicant_code)
        interview_list = self.__select_interview_by_app_code(applicant_code)
        max_length = self.__search_longest_element(interview_list)
        self.__print_interview(interview_list, max_length)

    def filter_by_mentor_code(self):
        mentor_id = self.__input_id("mentor id")
        self.__check_mentor_id(mentor_id)
        interview_list = self.__select_interview_by_mentor_id(mentor_id)
        max_length = self.__search_longest_element(interview_list)
        self.__print_interview(interview_list, max_length)

    def filter_by_date(self):
        date_from = self.__input_datetime()
        date_to = self.__input_datetime()
        interview_list = self.__select_interview_by_date(date_from, date_to)
        max_length = self.__search_longest_element(interview_list)
        self.__print_interview(interview_list, max_length)

    def __input_id(self, id_type):
        id_ = input("Please add me the {0}: ".format(id_type))
        return id_

    def __input_datetime(self):
        y = int(input("Please add a year: "))
        m = int(input("Please add a month: "))
        d = int(input("Please add a day: "))
        return datetime(y, m, d)

    def __add_header(self):
        applicants_list = [["Start time", "End time", "Reserved", "Mentor name", "City"]]
        return applicants_list

    def __select_interview_by_school(self, school_id):
        interview_list = self.__add_header()
        interview_slot = InterviewSlot.select()
        for slot in interview_slot:
            if int(school_id) == slot.mentor.school.id:
                interview_list.append([slot.start_time, slot.end_time, slot.reserved, slot.mentor.last_name, slot.mentor.school.city])

        return interview_list

    def __select_interview_by_app_code(self, applicant_code):
        interview_list = self.__add_header()
        interview_slot = InterviewSlot.select()

        for slot in interview_slot:
            for interview in slot.interviews:
                if str(applicant_code) == interview.applicant_code.applicant_code:
                    interview_list.append([slot.start_time, slot.end_time, slot.reserved, slot.mentor.last_name,
                                           slot.mentor.school.city])
        return interview_list

    def __select_interview_by_mentor_id(self, mentor_id):
        interview_list = self.__add_header()
        mentors = Mentor.select()

        for mentor in mentors:
            for int_slot in mentor.interview_slots:
                if int(mentor_id) == int_slot.mentor.id:
                    interview_list.append([int_slot.start_time, int_slot.end_time, int_slot.reserved,
                                           int_slot.mentor.last_name, int_slot.mentor.school.city])
        return interview_list

    def __select_interview_by_date(self, date_from, date_to):
        interview_list = self.__add_header()
        interviews_slot = InterviewSlot.select()

        for slot in interviews_slot:
            if slot.start_time > date_from and slot.end_time < date_to:
                interview_list.append([slot.start_time, slot.end_time, slot.reserved,
                                      slot.mentor.last_name, slot.mentor.school.city])
        return interview_list

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

    def __search_longest_element(self, example_list):
        max_length = 0
        for sublist in example_list:
            for element in sublist:
                if len(str(element)) > max_length:
                    max_length = len(str(element))
        return max_length

    def __print_interview(self, interview_list, max_length):
        for sublist in interview_list:
            print()
            for element in sublist:
                print(str(element).center(max_length), end=", ")
        print()
