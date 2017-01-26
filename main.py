import os


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
                print("- - - School system - Administrator Menu - - -")
                print("1. ")
                print("2. ")
                print("3. ")
                print("0. Exit")
                print("-------------------------------------")
                chosen_administrator_menu = int(input("Please choose an Administrator menu number: "))

                if chosen_administrator_menu == 1:
                    # call mentor menu
                    pass

                elif chosen_administrator_menu == 2:
                    # call mentor menu
                    pass

                elif chosen_administrator_menu == 3:
                    # call applicant menu
                    pass

                elif chosen_administrator_menu == 0:
                    break

                else:
                    print("Wrong menu number was given")



        elif chosen_menu == 2:
            clear_sreen()
            chosen_mentor_menu = 'q'
            while chosen_mentor_menu != 0:
                print("\n- - - School system - Mentor Menu - - -")
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
                    break

                else:
                    print("Wrong menu number was given")

        elif chosen_menu == 3:
            clear_sreen()
            chosen_applicant_menu = 'q'
            while chosen_applicant_menu != 0:
                print("\n- - - School system - Applicant Menu - - -")
                print("1. ")
                print("2. ")
                print("3. ")
                print("0. Exit")
                print("-------------------------------------")
                chosen_applicant_menu = int(input("Please choose an Applicant menu number: "))

                if chosen_menu == 1:
                    # call mentor menu
                    pass

                elif chosen_menu == 2:
                    # call mentor menu
                    pass

                elif chosen_menu == 3:
                    # call applicant menu
                    pass

                elif chosen_menu == 0:
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
