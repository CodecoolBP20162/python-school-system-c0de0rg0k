from generator.build_table import BuildTable
from UserInterface import UserInterface
from Applicant import ApplicantQueries
from generator.applicant_generator import ApplicantGenerator
from mentor_queries import MentorQueries
from administrator_queries_interviews import AdministratorQueriesInterviews


class Main:

    def __init__(self):
        self.ui = UserInterface()
        self.build_table = BuildTable()
        self.applicant_generator = ApplicantGenerator()
        self.applicant_queries = ApplicantQueries()
        self.mentor_queries = MentorQueries()
        self.administrator_filter_interviews = AdministratorQueriesInterviews()

    def main(self):
        self.ui.clear_sreen()
        chosen_menu = ''
        while chosen_menu != '0':
            self.ui.print_main_menu()
            chosen_menu = self.ui.print_choose_menu("main")
            if chosen_menu == '1':
                self.administrator_menu()
            elif chosen_menu == '2':
                self.mentor_menu()
            elif chosen_menu == '3':
                self.applicant_menu()
            elif chosen_menu == '0':
                self.ui.print_exit_program()
            else:
                self.ui.print_wrong_menu_chosen()

    def administrator_menu(self):
        self.ui.clear_sreen()
        chosen_administrator_menu = ''
        while chosen_administrator_menu != '0':
            self.ui.print_administrator_menu()
            chosen_administrator_menu = self.ui.print_choose_menu("administrator")
            if chosen_administrator_menu == '1':
                try:
                    self.build_table.build_table()
                    self.ui.built_tables_successfully()
                except:
                    self.ui.build_tables_failed()
            elif chosen_administrator_menu == '2':
                try:
                    self.build_table.generate_example_data()
                    self.ui.generated_data_successfully()
                except:
                    self.ui.generate_data_failed()
            elif chosen_administrator_menu == '3':
                try:
                    self.applicant_generator.generate_applicant()
                    self.applicant_generator.generate_nearest_school()
                    self.ui.generated_data_successfully()
                except:
                    self.ui.generate_data_failed()
            elif chosen_administrator_menu == '4':
                try:
                    self.applicant_generator.generate_interview_for_applicants()
                    self.ui.generated_data_successfully()
                except:
                    self.ui.generate_data_failed()
            elif chosen_administrator_menu == '5':
                self.ui.clear_sreen()
                chosen_administrator_filter_menu = ''
                while chosen_administrator_filter_menu != '0':
                    self.ui.administrator_filter_interviews()
                    administrator_filter_submenu = self.ui.print_choose_menu("administrator - filter")
                    if administrator_filter_submenu == '1':
                        try:
                            self.administrator_filter_interviews.filter_by_school()
                        except:
                            self.ui.print_wrong_data("school id")
                    elif administrator_filter_submenu == '2':
                        try:
                            self.administrator_filter_interviews.filter_by_applicant_code()
                        except:
                            self.ui.print_wrong_data("applicant code")
                    elif administrator_filter_submenu == '3':
                        try:
                            self.administrator_filter_interviews.filter_by_mentor_code()
                        except:
                            self.ui.print_wrong_data("mentor id")
                    elif administrator_filter_submenu == '4':
                        try:
                            self.administrator_filter_interviews.filter_by_date()
                        except:
                            self.ui.print_wrong_data("date")
                    elif administrator_filter_submenu == '0':
                        self.ui.clear_sreen()
                        break
                    else:
                        self.ui.print_wrong_menu_chosen()
            elif chosen_administrator_menu == '0':
                self.ui.clear_sreen()
                break
            else:
                self.ui.print_wrong_menu_chosen()

    def mentor_menu(self):
        self.ui.clear_sreen()
        chosen_mentor_menu = ''
        while chosen_mentor_menu != '0':
            self.ui.print_mentor_menu()
            chosen_mentor_menu = self.ui.print_choose_menu("mentor")
            if chosen_mentor_menu == '1':
                self.mentor_queries.mentor_date_time()
            elif chosen_mentor_menu == '0':
                self.ui.clear_sreen()
                break
            else:
                self.ui.print_wrong_menu_chosen()

    def applicant_menu(self):
        self.ui.clear_sreen()
        chosen_applicant_menu = ''
        while chosen_applicant_menu != '0':
            self.ui.print_applicant_menu()
            chosen_applicant_menu = self.ui.print_choose_menu("applicant")
            if chosen_applicant_menu == '1':
                self.applicant_queries.interview_details()
            elif chosen_applicant_menu == '2':
                self.applicant_queries.status_details()
            elif chosen_applicant_menu == '3':
                self.applicant_queries.school_details()
            elif chosen_applicant_menu == '4':
                self.applicant_queries.ask_question()
            elif chosen_applicant_menu == '0':
                self.ui.clear_sreen()
                break
            else:
                self.ui.print_wrong_menu_chosen()

if __name__ == '__main__':
    Main().main()