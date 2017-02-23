from random import randint
from models import *


class AppCodeGenerator:
    """This class generate the application code. First, generate the application_code, then compare the earlier password
       if the current app code equal with the earlier, generate a new one"""

    def code_generator(self):
        earlier_app_code = self.__query_the_earliest_app_code()
        new_code = self.__code_generator()
        is_valid = False

        while is_valid is False:
            new_code = self.__code_generator()
            is_valid = self.__check_earlier_app_code(new_code, earlier_app_code)
        return new_code

    def __query_the_earliest_app_code(self):
        earlier_app_code = []
        applications = Applicant.select()
        for application in applications:
            earlier_app_code.append(application.applicant_code)
        return earlier_app_code

    def __code_generator(self):
        application_code = ""
        counter = 0
        while counter != 6:
            application_code += str(randint(0, 9))
            counter += 1
        return application_code

    def __check_earlier_app_code(self, new_code, earlier_app_code_list):
        if new_code not in earlier_app_code_list:
            return True
        else:
            return False
