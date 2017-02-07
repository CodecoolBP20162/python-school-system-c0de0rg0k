
class SetConnection:

    def __init__(self, file_name='connect.txt'):
        self.file_name = file_name
        self.username = ""
        self.dbname = ""

        self.__read_files()

    def __read_files(self):
        with open(self.file_name) as f:
            line = f.readline().split(",")
            if len(line) == 1:
                self.username = line[0]
            else:
                self.dbname = line[0]
                self.username = line[1]
