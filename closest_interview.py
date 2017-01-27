"""Write a script that chooses the closest interview date based on the availability of mentors
   (using the InterviewSlot model) and reserve it """
from models import *
from datetime import datetime


class ApplicantGenerator:

    def __init__(self):
        # !!!this update the interview table with applicants objects
        applicants = Applicant.select()
        for applicant in applicants:
            new_interview = Interview.create(applicant_code=applicant)

        self.__interview_update()

    def __interview_update(self):
        interviews = Interview.select()
        int_slot = InterviewSlot.select().where(InterviewSlot.start_time > datetime.now())

        for interview in interviews:
            for slot in int_slot:
                if interview.applicant_code.applied_school.city == slot.mentor.school.city and slot.reserved is False:
                    slot.reserved = True
                    slot.save()
                    interview.slot_id = slot
                    interview.save()
                    break
