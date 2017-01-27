from models import *

#Write the queries, which give back the applicants's school, date time and the interviewing mentor name

def Interview_details():
    application_code = input("Please, enter your application code: ")
    query = Interview.select().join(Applicant).where(Applicant.applicant_code==application_code)
    if len(query)==0:
        print("Wrong code! Please, try again!")
    for i in query:
        print(i.applicant_code.first_name, i.applicant_code.last_name, "\n",
              "Your school is Codecool", i.applicant_code.applied_school.city, "\n",
              "Your interview date:", i.slot_id.start_time, "\n",
              "Your mentor is", i.slot_id.mentor.first_name, i.slot_id.mentor.last_name)



