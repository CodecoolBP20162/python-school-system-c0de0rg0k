from generator.app_code_generator import AppCodeGenerator
from models import *


class ApplicantGenerator:
    """ First, generate the applicants: read from the file, then update the Applicant table with the applicants_list
        Secondly, generate the nearest school: read the applicants from the table, and assign the nearest school_id to the table
        based on the City table nearest_School column.
        If every applicants has the nearest school id, we can call generate interview method,
        which update the Interview table with applicant, then update the Interview table with the
        suitable slot_id """

    def __init__(self, file_name="example_data/applicant.txt"):
        self.file_name = file_name

    def generate_applicant(self):
        applicants_list = self.__read_applicant_from_file()
        self.__update_applicant_table(applicants_list)
        self.__generate_application_code()

    def generate_nearest_school(self):
        applicants = Applicant.select().where(Applicant.applied_school.is_null(True))
        for applicant in applicants:
            closest_city = self.__search_nearest_school(applicant.applicant_city)
            applicant.applied_school = closest_city
            applicant.save()

    def generate_interview_for_applicants(self):
        applicants = Applicant.select()
        for applicant in applicants:
            Interview.create(applicant_code=applicant)

        self.__search_mentor_for_interviewslot()

    def __read_applicant_from_file(self):
        with open(self.file_name, "r") as f:
            lines = f.readlines()
            applicant_list = []

            for line in lines:
                applicant_list.append(line.strip().split(";"))

        return applicant_list

    def __update_applicant_table(self, applicants_list):
        for applicant in applicants_list:
            Applicant.create(first_name=applicant[0], last_name=applicant[1], applicant_city=applicant[2],
                             status=applicant[3])

    def __search_nearest_school(self, application_city):
        current_city = City.get(city_name=application_city)
        return current_city.nearest_school

    def __search_mentor_for_interviewslot(self):
        interviews = Interview.select()
        int_slot = InterviewSlot.select().where(InterviewSlot.start_time > "2017-01-30 12:00:00")

        for interview in interviews:
            for slot in int_slot:
                if interview.applicant_code.applied_school.city == slot.mentor.school.city and slot.reserved is False:
                    slot.reserved = True
                    slot.save()
                    interview.slot_id = slot
                    interview.save()
                    break

    def __generate_application_code(self):
        applicants = Applicant.select()
        for applicant in applicants:
            # Create an instance, and the current applicant (from the table) get the generated application_code
            new_app_code = AppCodeGenerator()
            applicant.applicant_code = new_app_code.code_generator()
            applicant.save()
