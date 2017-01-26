from peewee import *
from models import *


class GenerateSchool:

    def __init__(self, application_city):
        current_city = City.get(city_name=application_city)
        self.nearest_school = current_city.nearest_school
