from random import randint
# az erliar_app_code mindig lekérdezhetné az application code-okat
# és tegyem ciklusba a probálkozást, és addig ne hozzon létre, amíg van olyan appcode a listában


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
        counter = 0
        while counter != 6:
            self.application_code += str(randint(0, 10))

            counter += 1

    def __check_earlier_app_code(self):
        # if the current password in the earlier, add plus 1 to the current
        for password in self.__earlier_app_code:
            if self.application_code == password:
                self.application_code += "1"
