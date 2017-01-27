from models import *

class MentorInterviewDate:

    def __init__(self, mentor_id):
        self.mentor_interview_slot = ""
        self.mentor_id = mentor_id
        self.__select_mentor()
        self.__print_datetime()

    def __select_mentor(self):
        self.mentor_interview_slot = InterviewSlot.select()


    def __print_datetime(self):
        for slot in self.mentor_interview_slot:
            if self.mentor_id == slot.mentor.id:
                for interview in Interview.select().where(Interview.slot_id == slot.id):
                    print(slot.start_time, interview.applicant_code.first_name, interview.applicant_code.last_name,
                          interview.applicant_code.applicant_code)
