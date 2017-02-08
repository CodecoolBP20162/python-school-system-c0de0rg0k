
class SetConnection:

    def __init__(self, file_name='connect.txt'):
        self.username = ""
        with open(file_name) as f:
            self.username = f.read()
