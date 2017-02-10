from models import *
from datetime import datetime


class AdministratorQueriesApplicants:
    """This class filter the applicants by the following criteria (status, school location, applicant name, school id
        time and mentor name"""

    def show_applicants(self):
        applicants = Applicant.select()
        applicants_list = self.__add_header()

        for app in applicants:
            applicants_list.append([app.first_name, app.last_name, app.applicant_city, app.applied_school.city, app.applicant_code, app.status])

        max_length = self.__search_longest_element(applicants_list)
        self.__print_applicants(applicants_list, max_length)

    def filter_by_status(self):
        asked_status = self.__input_identification('status')
        applicants_list = self.__select_applicants_by_status(asked_status)
        max_length = self.__search_longest_element(applicants_list)
        self.__print_applicants(applicants_list, max_length)

    def filter_by_location(self):
        asked_location = self.__input_identification('location')
        applicants_list = self.__select_applicants_by_location(asked_location)
        max_length = self.__search_longest_element(applicants_list)
        self.__print_applicants(applicants_list, max_length)

    def filter_by_name(self):
        asked_full_name = self.__input_identification('first and last name')
        applicants_list = self.__select_applicants_by_name(asked_full_name)
        max_length = self.__search_longest_element(applicants_list)
        self.__print_applicants(applicants_list, max_length)

    def filter_by_school(self):
        asked_school_id = self.__input_identification('school id')
        applicants_list = self.__select_applicants_by_school_id(asked_school_id)
        max_length = self.__search_longest_element(applicants_list)
        self.__print_applicants(applicants_list, max_length)

    def filter_by_time(self):
        asked_from_datetime = self.__input_datetime()
        asked_to_datetime = self.__input_datetime()
        applicants_list = self.__select_applicants_by_time(asked_from_datetime, asked_to_datetime)
        max_length = self.__search_longest_element(applicants_list)
        self.__print_applicants(applicants_list, max_length)

    def filter_by_mentor_name(self):
        masked_mentor_name = self.__input_identification('mentor name')
        applicants_list = self.__select_applicants_by_mentor_name(masked_mentor_name)
        max_length = self.__search_longest_element(applicants_list)
        self.__print_applicants(applicants_list, max_length)

    def __input_identification(self, identification):
        id_ = input("Please add me your {0}: ".format(identification))
        return id_

    def __input_datetime(self):
        y = int(input("Please add a year: "))
        m = int(input("Please add a month: "))
        d = int(input("Please add a day: "))
        h = int(input("Please add the hour: "))
        return datetime(y, m, d, h)

    def __search_longest_element(self, example_list):
        max_length = 0
        for sublist in example_list:
            for element in sublist:
                if len(str(element)) > max_length:
                    max_length = len(str(element))
        return max_length

    def __add_header(self):
        applicants_list = [["First name", "Last name", "Applicant city", "Applied school", "Applicant code", "Status"]]
        return applicants_list

    def __select_applicants_by_time(self, from_date, from_to):
        interviews = Interview.select().join(InterviewSlot)
        applicants_list = self.__add_header()

        for interview in interviews:
            if from_date < interview.slot_id.start_time and from_to > interview.slot_id.end_time \
                    and interview.slot_id.reserved is True:
                applicants_list.append([interview.applicant_code.first_name, interview.applicant_code.last_name, interview.applicant_code.applicant_city,
                      interview.applicant_code.applied_school.city, interview.applicant_code.applicant_code, interview.applicant_code.status])

        return applicants_list

    def __select_applicants_by_status(self, asked_id):
        applicants = Applicant.select().where(Applicant.status == asked_id)
        applicants_list = self.__add_header()

        for app in applicants:
            applicants_list.append([app.first_name, app.last_name, app.applicant_city, app.applied_school.city, app.applicant_code, app.status])
        return applicants_list

    def __select_applicants_by_location(self, location):
        applicants = Applicant.select()
        applicants_list = self.__add_header()

        for app in applicants:
            if location == app.applied_school.city:
                applicants_list.append([app.first_name, app.last_name, app.applicant_city, app.applied_school.city, app.applicant_code, app.status])
        return applicants_list

    def __select_applicants_by_name(self, full_name):
        name_list = full_name.split(" ")
        applicants = Applicant.select().where(Applicant.first_name == name_list[0] and
                                              Applicant.last_name == name_list[1])
        applicants_list = self.__add_header()

        for app in applicants:
            applicants_list.append([app.first_name, app.last_name, app.applicant_city, app.applied_school.city, app.applicant_code, app.status])
        return applicants_list

    def __select_applicants_by_school_id(self, school_id):
        applicants = Applicant.select().where(Applicant.applied_school == school_id)
        applicants_list = self.__add_header()

        for app in applicants:
            applicants_list.append([app.first_name, app.last_name, app.applicant_city, app.applied_school.city, app.applicant_code, app.status])
        return applicants_list

    def __select_applicants_by_mentor_name(self, mentor_name):
        interviews = Interview.select().join(InterviewSlot)
        applicants_list = self.__add_header()

        for interview in interviews:
            if interview.slot_id.mentor.last_name == mentor_name:
                applicants_list.append([interview.applicant_code.first_name, interview.applicant_code.last_name,
                      interview.applicant_code.applicant_city, interview.applicant_code.applied_school.city, interview.applicant_code.applicant_code, interview.applicant_code.status])

        return applicants_list

    def __print_applicants(self, app_list, max_length):
        for sublist in app_list:
            print()
            for element in sublist:
                print(element.center(max_length), end=", ")
        print()
