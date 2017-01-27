import os
#from applicants_status import applicants_status
from build import BuildTable
from example_data import GenerateExampleData
from new_applicants import GenerateApplicants
from applicants_school import applicants_school
#from sort_applicants import sort_applicants
from closest_interview import ApplicantGenerator
from applicant_interview_details import *


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
            clear_sreen()
            chosen_administrator_menu = 'q'
            while chosen_administrator_menu != 0:
                print("\n- - - School system - Administrator Menu - - -\n-------------------------------------")
                print("1. Create tables")
                print("2. Generate data")
                print("3. Generate applicants")
                print("4. Generate interview date to applicants")
                print("5. List all applicants")
                print("0. Exit")
                print("-------------------------------------")
                chosen_administrator_menu = int(input("Please choose an Administrator menu number: "))

                if chosen_administrator_menu == 1:
                    try:
                        BuildTable()
                        print("Tables created succcessfully")
                    except:
                        print("I can't create tables")

                elif chosen_administrator_menu == 2:
                    try:
                        GenerateExampleData()
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

                elif chosen_administrator_menu == 5:
                    clear_sreen()
                    print("\n- - - School system - Administrator Menu - Sort applicants - - -\n-------------------------------------")
                    print("1. By Status")
                    print("2. By Time")
                    print("3. By Location")
                    print("4. By Personal data (name, email)")
                    print("5. By School")
                    print("6. By Mentor name")
                    print("0. Exit")
                    print("-------------------------------------")
                    chosen_sort_menu = input("Choose a menu number to sort applicants: ")
                    if chosen_sort_menu == 1:
                        ordered_applicants = sort_applicants("status")
                    elif chosen_sort_menu == 2:
                        pass
                    elif chosen_sort_menu == 3:
                        ordered_applicants = sort_applicants()
                        print(ordered_applicants)
                        for applicant in ordered_applicants:
                            print(applicant.id, applicant.first_name, applicant.last_name, applicant.applicant_city /
                                  applicant.applicant_code, applicant.status)
                    elif chosen_sort_menu == 4:
                        pass
                    elif chosen_sort_menu == 5:
                        pass
                    elif chosen_sort_menu == 6:
                        pass
                    elif chosen_sort_menu == 0:
                        clear_sreen()
                        break

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
                print("1. ")
                print("2. ")
                print("3. ")
                print("0. Exit")
                print("-------------------------------------")
                chosen_mentor_menu = int(input("Please choose a Mentor menu number: "))

                if chosen_mentor_menu == 1:
                    # call mentor menu
                    pass

                elif chosen_mentor_menu == 2:
                    # call mentor menu
                    pass

                elif chosen_mentor_menu == 3:
                    # call mentor menu
                    pass

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
                print("1. Application details")
                print("2. School details")
                print("3. Questions")
                print("0. Exit")
                print("-------------------------------------")
                chosen_applicant_menu = int(input("Please choose an Applicant menu number: "))

                if chosen_applicant_menu == 1:
                        Interview_details()

                elif chosen_applicant_menu == 2:
                    try:
                        pass
                    except:
                        print("There is no application code like that in the database. Please try again")

                elif chosen_applicant_menu == 3:
                    # call applicant menu
                    pass

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


main()
