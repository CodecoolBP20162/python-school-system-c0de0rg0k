# This script can generate example data for "City" and "InterviewSlot" models.

from models import *

CC_Budapest = School.create(id=1, city='Budapest')
CC_Miskolc = School.create(id=2, city='Miskolc')
CC_Krakow = School.create(id=3, city='Krakow')

Budapest = City.create(city_name='Budapest', nearest_school=CC_Budapest)
Miskolc = City.create(city_name='Miskolc', nearest_school=CC_Miskolc)
Krakow = City.create(city_name='Krakow', nearest_school=CC_Krakow)