import os
from applicantdfcants import GenerateApplicants
from appdfgdfgprint("2. I am a mentor")
        print("3. I am an applicant")
        print("0. Exit")
        print("-------------------------------")
        chosen_menu = int(input("Please choose a menu number: "))

        if chosen_menu == 1:
    drgd        # Create instance
            build_and_upload_tables = BuildTable()
            clear_sreen()
            chosen_administrator_menu = 'q'
            while chosen_administrator_menu != 0:
                print("\n- - - School system - Administrator Menu - - -\n-------------------------------------")
                print("1. Create tables")
                print("2. Generate data")
                print("3. Generate applicants")
                print("4. Generate interview date to applicants")
                print("0. Exit")
                print("-------------------------------------")
                chosen_administrator_menu = int(input("Please choose an Administrator menu number: "))
dd         except:
                        print("I can't create tables")

                elif chosen_administrator_menu == 2:
                    try:
                        build_and_upload_tables.generate_example_data()
                        print("Data successfully generated and inserted")
                    except:
                      a
                elif chosen_administrator_menu == 4:
                    try:
                        ApplicantGenerator()
                        print("Interview dates successfully generated to applicants")
                    except:
                        print("Something went wrong. I can't generate interview dates to applicants")

                elif chosen_administrator_menu == 0:
                    clear_sreen()
                    break

                else:
                    print("Wrong menu number was given")



        elif chosen_menu == 2:
            clear_sreen()
            chosen_mentor_menu = 'q'
            while chosen_mentor_menu != 0:
                print("\n- - - School system - Mentor Menu - - -\n-------------------------------------")
                print("1. Interviews")
                print("0. Exit")
                print("-------------------------------------")
                chosen_mentor_menu = int(input("Please choose a Mentor menu number: "))
                if chosen_mentor_menu == 1:
                    mentor_id = int(input("Please tell me your mentor id: "))
                    try:
                        MentorInterviewDate(mentor_id)
                    except:
                chosen_applicant_menu = int(input("Please choose an Applicant menu number: "))

                if chosen_applicant_menu == 1:
                    interview_details()
                elif chosen_applicant_menu == 2:
                    application_code = input("Please, enter your application code: ")
                    try:
                        status = applicants_status(application_code)
                        print("Your application status is", status)
                    except:
                        print("There is no application code like that in the database. Please try again")
                elif chosen_applicant_menu == 0:
                    clear_sreen()
                    break

                else:
      dfg              print("Wrong menu number was given")
dddd
drftgdf
dfgfdg