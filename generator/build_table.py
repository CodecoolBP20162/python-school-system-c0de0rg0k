from models import *


class BuildTable:
    """This class create table and generate the example data from files (example_data/)"""

    def __init__(self, city_file_name="example_data/city.txt", school_file_name="example_data/school.txt",
                 mentors_file_name="example_data/mentor.txt",
                 interviewslot_file_name="example_data/interviewslot.txt"):

        # First create the tables
        self.city_file_name = city_file_name
        self.school_file_name = school_file_name
        self.mentors_file_name = mentors_file_name
        self.interviewslot_file_name = interviewslot_file_name

    def build_table(self):
        try:
            db.connect()
        except:
            print('I can\'t connect to the database')

        if School.table_exists():
            School.drop_table(cascade=True)

        if Applicant.table_exists():
            Applicant.drop_table(cascade=True)

        if City.table_exists():
            City.drop_table(cascade=True)

        if Mentor.table_exists():
            Mentor.drop_table(cascade=True)

        if InterviewSlot.table_exists():
            InterviewSlot.drop_table(cascade=True)

        if Interview.table_exists():
            Interview.drop_table(cascade=True)

        if Q_A.table_exists():
            Q_A.drop_table(cascade=True)

        if EmailDetails.table_exists():
            EmailDetails.drop_table(cascade=True)

        db.create_tables([School, Applicant, City, Mentor, InterviewSlot, Interview, Q_A, EmailDetails], safe=True)

    def generate_example_data(self):
        schools_list = self.__read_data_from_file(self.school_file_name)
        self.__upload_school_table(schools_list)

        cities_list = self.__read_data_from_file(self.city_file_name)
        self.__upload_city_table(cities_list)

        mentors_list = self.__read_data_from_file(self.mentors_file_name)
        self.__upload_mentor_table(mentors_list)

        interview_slot_list = self.__read_data_from_file(self.interviewslot_file_name)
        self.__upload_interviewslot_table(interview_slot_list)

    def __read_data_from_file(self, file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            data_list = []
            for line in lines:
                data_list.append(line.strip().split(";"))

        return data_list

    def __upload_school_table(self, schools_list):
        for school in schools_list:
            School.create(city=school[0])

    def __upload_city_table(self, cities_list):
        for city in cities_list:
            City.create(city_name=city[0], nearest_school_id=city[1])

    def __upload_mentor_table(self, mentors_list):
        for mentor in mentors_list:
            Mentor.create(first_name=mentor[0], last_name=mentor[1], school=mentor[2])

    def __upload_interviewslot_table(self, interview_slot_list):
        for slot in interview_slot_list:
            x = InterviewSlot.create(start_time=slot[0], end_time=slot[1], reserved=bool(int(slot[2])), mentor=slot[3])