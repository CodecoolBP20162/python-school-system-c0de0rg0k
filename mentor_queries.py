from models import *


class MentorQueries:
    """This class give back the necessary details for the mentors menu"""

    def __init__(self):
        self.mentor_id = 0

    def mentor_date_time(self):
        self.__input_mentor_id()
        self.__check_mentor_id()        # Check the mentor id, raise error if that mentor_id is not in the table
        self.__print_datetime()

    def __input_mentor_id(self):
        self.mentor_id = int(input("Please tell me your mentor id: "))

    def __check_mentor_id(self):
        mentors = Mentor.select().where(Mentor.id == self.mentor_id)
        if len(mentors) == 0:
            raise ValueError

    def __print_datetime(self):
        interview_slot = InterviewSlot.select()
        for slot in interview_slot:
            if self.mentor_id == slot.mentor.id:
                for interview in Interview.select().where(Interview.slot_id == slot.id):
                    print(slot.start_time, interview.applicant_code.first_name, interview.applicant_code.last_name,
                          interview.applicant_code.applicant_code)
