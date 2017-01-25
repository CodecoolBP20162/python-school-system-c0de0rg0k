from random import randint


class GenerateAppCode:
    """This class generate the application code"""
    __earlier_app_code = []

    def __init__(self):
        # First, generate the application_code, then compare the earlier password with the current and
        # append the current to the earlier password list
        self.application_code = ""
        self.__code_generator()
        self.__check_earlier_app_code()
        self.__earlier_app_code.append(self.application_code)

    def __code_generator(self):
        # pass_ls_length = len(self.earlier_app_code) - 1
        # self.application_code = self.earlier_app_code[pass_ls_length] + 1

        counter = 0
        while counter != 6:
            self.application_code += str(randint(0, 10))

            counter += 1

    def __check_earlier_app_code(self):
        # if the current password in the earlier, add plus 1 to the current
        for password in self.__earlier_app_code:
            if self.application_code == password:
                self.application_code += "1"
