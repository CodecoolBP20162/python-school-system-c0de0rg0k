from peewee import *
from set_connection import SetConnection

from models import *


def findNearestSchool(city)
    current_city = City.get(city_name= city)
    current_nearest_school = current_city.nearest_school
    return current_nearest_school

