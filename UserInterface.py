import os


class UserInterface:

    def clear_sreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_main_menu(self):
        print("\n- - - School system - Main Menu - - -\n-------------------------------------")
        print("1. I am an administrator")
        print("2. I am a mentor")
        print("3. I am an applicant")
        print("4. I am new. I want to register")
        print("0. Exit")
        print("-------------------------------")

    def print_administrator_menu(self):
        print("\n- - - School system - Administrator Menu - - -\n-------------------------------------")
        print("1. Create tables")
        print("2. Generate data")
        print("3. Generate applicants")
        print("4. Generate interview date to applicants")
        print("5. Filter scheduled interviews")
        print("0. Exit")
        print("-------------------------------------")

    def print_mentor_menu(self):
        print("\n- - - School system - Mentor Menu - - -\n-------------------------------------")
        print("1. Interviews")
        print("0. Exit")
        print("-------------------------------------")

    def print_applicant_menu(self):
        print("\n- - - School system - Applicant Menu - - -\n-------------------------------------")
        print("1. Interview details")
        print("2. Status details")
        print("3. School details")
        print("0. Exit")
        print("-------------------------------------")

    def administrator_filter_interviews(self):
        print("\n- - - School system - Administrator Menu - Filter interviews - - -\n-------------------------------------")
        print("1. Filter by school")
        print("2. Filter by applicant code")
        print("3. Filter by mentor code")
        print("4. Filter by date (from - to (year - month - day))")
        print("0. Exit")
        print("-------------------------------------")

    def print_registration_menu(self):
        print("\n- - - School system - Registration menu - - -\n-------------------------------------")
        print("1. Register as new applicant")
        print("2. Register as new mentor")
        print("0. Exit")
        print("-------------------------------------")

    def print_choose_menu(self, menu_name):
        chosen_menu = input("Please choose a(n) {0} menu number: ".format(menu_name))
        return chosen_menu

    def built_tables_successfully(self):
        print("Tables created successfully")

    def build_tables_failed(self):
        print("I can't create tables")

    def generated_data_successfully(self):
        print("Data generated successfully")

    def generate_data_failed(self):
        print("Data generating failed")

    def data_inserted_successfully(self):
        print("Data inserted successfully")

    def data_insert_failed(self):
        print("Data inserting failed")

    def cant_find_in_database(self, user_type):
        print("I can't find {0} with this data in the database.".format(user_type))

    def print_wrong_menu_chosen(self):
        print("Wrong menu number was given")

    def print_wrong_data(self, data_type):
        print("Wrong {0} was given".format(data_type))

    def print_exit_program(self):
        print("\n------------------------------------------------------------")
        print("| Thanks for choosing Codeorgo Software! See you next time!|")
        print("------------------------------------------------------------")