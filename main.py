import os
from generator.build_table import BuildTable
from generator.applicant_generator import ApplicantGenerator
from mentor_queries import MentorQueries
from administrator_queries_interviews import AdministratorQueriesInterviews

def clear_sreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    chosen_menu = 'q'
    build_table = BuildTable()
    applicant_generator = ApplicantGenerator()

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
            clear_sreen()
            chosen_administrator_menu = 'q'
            while chosen_administrator_menu != 0:
                print("\n- - - School system - Administrator Menu - - -\n-------------------------------------")
                print("1. Create tables")
                print("2. Generate data")
                print("3. Generate applicants")
                print("4. Generate interview date to applicants")
                print("5. Interviews details")
                print("0. Exit")
                print("-------------------------------------")
                chosen_administrator_menu = int(input("Please choose an Administrator menu number: "))
                if chosen_administrator_menu == 1:
                    try:
                        build_table.build_table()
                        print("Tables created succcessfully")
                    except:
                        print("I can't create tables")

                elif chosen_administrator_menu == 2:
                    try:
                        build_table.generate_example_data()
                        print("Data successfully generated and inserted")
                    except:
                        print("I can't Generate example data")

                elif chosen_administrator_menu == 3:
                    try:
                        applicant_generator.generate_applicant()
                        applicant_generator.generate_nearest_school()
                        print("Applicants data successfully generated and inserted")
                    except:
                        print("I can't Generate applicants")

                elif chosen_administrator_menu == 4:
                    try:
                        applicant_generator.generate_interview_for_applicants()
                        print("Interview dates successfully generated to applicants")
                    except:
                        print("Something went wrong. I can't generate interview dates to applicants")


                elif chosen_administrator_menu == 5:
                    chosen_adm_submenu = 'q'

                    while chosen_adm_submenu != '0':
                        print("\n- - - School system - Administrator Menu - - -\n-------------------------------------")
                        print("1. Filter by school")
                        print("2. Filter by applicant code")
                        print("3. Filter by mentor code")
                        print("4. Filter by date (from - to (year - month - day))")
                        print("0. Exit")
                        print("-------------------------------------")

                        chosen_adm_submenu = input("Please choose a number: ")
                        if chosen_adm_submenu == '1':
                            try:
                                AdministratorQueriesInterviews().filter_by_school()
                            except:
                                print("Wrong number")

                        elif chosen_adm_submenu == '2':
                            try:
                                AdministratorQueriesInterviews().filter_by_applicant_code()
                            except:
                                print("Wrong number")

                        elif chosen_adm_submenu == '3':
                            try:
                                AdministratorQueriesInterviews().filter_by_mentor_code()
                            except:
                                print("Wrong number")

                        elif chosen_adm_submenu == '4':
                            try:
                                AdministratorQueriesInterviews().filter_by_date()
                            except:
                                print("Wrong number")
                        else:
                            print ("Wrong number")

                elif chosen_administrator_menu == 0:
                    clear_sreen()
                    break

                else:
                    print("Wrong menu number was given")


        elif chosen_menu == 2:
            mentor_queries = MentorQueries()
            clear_sreen()
            chosen_mentor_menu = 'q'
            while chosen_mentor_menu != 0:
                print("\n- - - School system - Mentor Menu - - -\n-------------------------------------")
                print("1. Interviews")
                print("0. Exit")
                print("-------------------------------------")
                chosen_mentor_menu = int(input("Please choose a Mentor menu number: "))
                if chosen_mentor_menu == 1:
                    try:
                        mentor_queries.mentor_date_time()
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
                    # calling the interview seacrh by app code
                    pass
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

my_list = [1, 2, 3, 554, 23, 565, 33]

sum = 0

for n in my_list:
    sum = sum + n

print(sum)