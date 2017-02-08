import os
from applicants_status import applicants_status
from generator.build_table import BuildTable
from new_applicants import GenerateApplicants
from applicants_school import applicants_school
from closest_interview import ApplicantGenerator
from applicant_interview_details import *
from mentor_queries import MentorQueries


def clear_sreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    chosen_menu = 'q'

    clear_sreen()
    while chosen_menu != 0:
        print("\n- - - School system - Main Menu - - -\n-------------------------------------")
        print("1. I am an administrator")
        print("2. I am a mentor")
        print("3. I am an applicant")
        print("0. Exit")
        print("-------------------------------")
        chosen_menu = int(input("Please choose a menu number: "))

        if chosen_menu == 1:
            # Create instance
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

                if chosen_administrator_menu == 1:
                    try:
                        build_and_upload_tables.build_table()
                        print("Tables created succcessfully")
                    except:
                        print("I can't create tables")

                elif chosen_administrator_menu == 2:
                    try:
                        build_and_upload_tables.generate_example_data()
                        print("Data successfully generated and inserted")
                    except:
                        print("I can't Generate example data")

                elif chosen_administrator_menu == 3:
                    try:
                        GenerateApplicants()
                        print("Applicants data successfully generated and inserted")
                    except:
                        print("I can't Generate applicants")

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
                    mentor_id = MentorQueries()
                    try:
                        MentorInterviewDate(mentor_id)
                    except:
                        print("There is no mentor with that id")

                elif chosen_mentor_menu == 0:
                    clear_sreen()
                    break

                else:
                    print("Wrong menu number was given")

        elif chosen_menu == 3:
            clear_sreen()
            chosen_applicant_menu = 'q'
            while chosen_applicant_menu != 0:
                print("\n- - - School system - Applicant Menu - - -\n-------------------------------------")
                print("1. Interview details")
                print("2. Status details")
                print("3. School details")
                print("0. Exit")
                print("-------------------------------------")
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

                elif chosen_applicant_menu == 3:
                    application_code = input("Please, enter your application code: ")
                    try:
                        school = applicants_school(application_code)
                        print("Your applied school is", school.city)
                    except:
                        print("There is no application code like that in the database. Please try again")
                elif chosen_applicant_menu == 0:
                    clear_sreen()
                    break

                else:
                    print("Wrong menu number was given")

        elif chosen_menu == 0:
            print("\n------------------------------------------------------------")
            print("| Thanks for choosing Codeorgo Software! See you next time!|")
            print("------------------------------------------------------------")
        else:
            print("Wrong menu number was given")


#main()

#build = BuildTable()
#build.build_table()
#build.generate_example_data()

city_schools = City.select(City, School).join(School).where(City.city_name.contains('e'))
for city in city_schools:
    print(city.city_name, city.nearest_school.city)