# This script can generate example data for "City" and "InterviewSlot" models.

from models import *

# Update the school table
CC_Budapest = School.create(city='Budapest')
CC_Miskolc = School.create(city='Miskolc')
CC_Krakow = School.create(city='Krakow')

# Update the city table
Budapest = City.create(city_name='Budapest', nearest_school=CC_Budapest)
Vac = City.create(city_name='Vác', nearest_school=CC_Budapest)
Erd = City.create(city_name='Érd', nearest_school=CC_Budapest)
Szolnok = City.create(city_name='Szolnok', nearest_school=CC_Budapest)
Százhalombatta = City.create(city_name='Százhalombatta', nearest_school=CC_Budapest)
Miskolc = City.create(city_name='Miskolc', nearest_school=CC_Miskolc)
Eger = City.create(city_name='Eger', nearest_school=CC_Miskolc)
Szerencs = City.create(city_name='Szerencs', nearest_school=CC_Miskolc)
Tiszaujvaros = City.create(city_name='Tiszaújváros', nearest_school=CC_Miskolc)
Tokaj = City.create(city_name='Tokaj', nearest_school=CC_Miskolc)
Mad = City.create(city_name='Mád', nearest_school=CC_Miskolc)
Krakow = City.create(city_name='Krakow', nearest_school=CC_Krakow)
Katowice = City.create(city_name='Katowice', nearest_school=CC_Krakow)
Wadowice = City.create(city_name='Wadowice', nearest_school=CC_Krakow)
Zawoja = City.create(city_name='Zawoja', nearest_school=CC_Krakow)
Iwkowa = City.create(city_name='Iwkowa', nearest_school=CC_Krakow)

# Update the mentor table
Zozi = Mentor.create(first_name='A', last_name='Zozi', school=CC_Budapest)
Immi = Mentor.create(first_name='B', last_name='Immi', school=CC_Budapest)
Laci = Mentor.create(first_name='C', last_name='Laci', school=CC_Budapest)
Matyi = Mentor.create(first_name='D', last_name='Matyi', school=CC_Budapest)
Robi = Mentor.create(first_name='E', last_name='robi', school=CC_Miskolc)
Imre = Mentor.create(first_name='F', last_name='Imre', school=CC_Miskolc)
Attila = Mentor.create(first_name='G', last_name='Attila', school=CC_Miskolc)
Pal = Mentor.create(first_name='H', last_name='Pál', school=CC_Miskolc)
Agnieszka = Mentor.create(first_name='I', last_name='Agnieszka', school=CC_Krakow)
Marcin = Mentor.create(first_name='H', last_name='Marcin', school=CC_Krakow)
Mateusz = Mentor.create(first_name='J', last_name='Mateusz', school=CC_Krakow)

# Update the interviewslot table
slot1 = InterviewSlot.create(start_time=datetime(2017, 1, 16, 12, 00),
                             end_time=datetime(2017, 1, 16, 13, 00),
                             reserved=True, mentor=Zozi)
slot2 = InterviewSlot.create(start_time=datetime(2017, 1, 16, 14, 00),
                             end_time=datetime(2017, 1, 16, 15, 00),
                             reserved=True, mentor=Matyi)
slot3 = InterviewSlot.create(start_time=datetime(2017, 1, 30, 12, 00),
                             end_time=datetime(2017, 1, 30, 13, 00),
                             reserved=False, mentor=Immi)
slot4 = InterviewSlot.create(start_time=datetime(2017, 1, 30, 14, 00),
                             end_time=datetime(2017, 1, 30, 15, 00),
                             reserved=False, mentor=Laci)
slot5 = InterviewSlot.create(start_time=datetime(2017, 1, 30, 12, 00),
                             end_time=datetime(2017, 1, 30, 13, 00),
                             reserved=False, mentor=Robi)
slot6 = InterviewSlot.create(start_time=datetime(2017, 1, 30, 14, 00),
                             end_time=datetime(2017, 1, 30, 15, 00),
                             reserved=False, mentor=Imre)
slot7 = InterviewSlot.create(start_time=datetime(2017, 1, 30, 12, 00),
                             end_time=datetime(2017, 1, 30, 13, 00),
                             reserved=False, mentor=Attila)
slot8 = InterviewSlot.create(start_time=datetime(2017, 1, 30, 14, 00),
                             end_time=datetime(2017, 1, 30, 15, 00),
                             reserved=False, mentor=Pál)
slot9 = InterviewSlot.create(start_time=datetime(2017, 1, 30, 12, 00),
                             end_time=datetime(2017, 1, 30, 13, 00),
                             reserved=False, mentor=Agnieszka)
slot10 = InterviewSlot.create(start_time=datetime(2017, 1, 30, 14, 00),
                              end_time=datetime(2017, 1, 30, 15, 00),
                              reserved=False, mentor=Marcin)
slot11 = InterviewSlot.create(start_time=datetime(2017, 1, 30, 14, 00),
                              end_time=datetime(2017, 1, 30, 15, 00),
                              reserved=False, mentor=Mateusz)
slot12 = InterviewSlot.create(start_time=datetime(2017, 2, 16, 12, 00),
                              end_time=datetime(2017, 2, 16, 13, 00),
                              reserved=False, mentor=Zozi)
slot13 = InterviewSlot.create(start_time=datetime(2017, 2, 16, 14, 00),
                              end_time=datetime(2017, 2, 16, 15, 00),
                              reserved=False, mentor=Matyi)
slot14 = InterviewSlot.create(start_time=datetime(2017, 2, 16, 12, 00),
                              end_time=datetime(2017, 2, 16, 13, 00),
                              reserved=False, mentor=Immi)
slot15 = InterviewSlot.create(start_time=datetime(2017, 2, 16, 14, 00),
                              end_time=datetime(2017, 2, 16, 15, 00),
                              reserved=False, mentor=Laci)
slot16 = InterviewSlot.create(start_time=datetime(2017, 2, 16, 12, 00),
                              end_time=datetime(2017, 2, 16, 13, 00),
                              reserved=False, mentor=Robi)
slot17 = InterviewSlot.create(start_time=datetime(2017, 2, 16, 14, 00),
                              end_time=datetime(2017, 2, 16, 15, 00),
                              reserved=False, mentor=Imre)
slot18 = InterviewSlot.create(start_time=datetime(2017, 2, 16, 12, 00),
                              end_time=datetime(2017, 2, 16, 13, 00),
                              reserved=False, mentor=Attila)
slot19 = InterviewSlot.create(start_time=datetime(2017, 2, 16, 14, 00),
                              end_time=datetime(2017, 2, 16, 15, 00),
                              reserved=False, mentor=Pál)
slot20 = InterviewSlot.create(start_time=datetime(2017, 2, 16, 12, 00),
                              end_time=datetime(2017, 2, 16, 13, 00),
                              reserved=False, mentor=Agnieszka)
slot21 = InterviewSlot.create(start_time=datetime(2017, 2, 16, 14, 00),
                              end_time=datetime(2017, 2, 16, 15, 00),
                              reserved=False, mentor=Marcin)
slot22 = InterviewSlot.create(start_time=datetime(2017, 2, 16, 14, 00),
                              end_time=datetime(2017, 2, 16, 15, 00),
                              reserved=False, mentor=Mateusz)
