from models import *


class AdministratorQueries:

    def __init__(self):
        pass

    def filter_by_school(self, school_id):
        self.__check_school_id(school_id)
        self.__print_interview_by_school_id()

    def filter_by_applicant_code(self, applicant_code):
        self.__check_applicant_code(applicant_code)
        self.__print_interview_details_by_app_code(applicant_code)

    def filter_by_mentor_code(self, mentor_id):
        self.__check_mentor_id(mentor_id)
        self.__print_interview_by_mentor_id(mentor_id)


    def __print_interview_by_school_id(self, school_id):
        interview_slot = InterviewSlot.select()
        for slot in interview_slot:
            if int(school_id) == slot.mentor.school.id:
                print(slot.mentor.school.city, slot.start_time, slot.end_time, slot.reserved, slot.mentor.last_name)

    def __print_interview_by_app_code(self, applicant_code):
        interview_slot = InterviewSlot.select()
        for slot in interview_slot:
            for interview in slot.interviews:
                if applicant_code == interview.applicant_code.applicant_code:
                    print(interview.applicant_code.first_name,
                           interview.applicant_code.last_name)
                    # ide még kiírni az interviewslot adatais is!!

    def __print_interview_by_mentor_id(self, mentor_id):
        mentors = Mentor.select()
        for mentor in mentors:
            for int_slot in mentor.interview_slots:
                # ezt itt befejezni!! még nem addoltam!
                if int(mentor_id)
                print (int_slot.start_time)


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

    def filter_by_date(self):
        pass


x = AdministratorQueries()
# x.filter_by_school(4)
# x.filter_by_applicant_code("100650")
x.filter_by_mentor_code(2)