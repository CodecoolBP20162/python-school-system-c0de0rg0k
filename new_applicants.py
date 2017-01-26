# New applicants arrive into your project database by this script.
# You can run it anytime to generate new data!

from models import *
from app_code_generator import GenerateAppCode
from closest_school import GenerateSchool

# Update the applicant table
Kovacs_Bela = Applicant.create(first_name='Béla', last_name='Kovács', applicant_city='Eger', status='new')
Keli_Geri = Applicant.create(first_name='Geri', last_name='Keli', applicant_city='Vác', status='new')
Kovari_Ivett = Applicant.create(first_name='Ivett', last_name='Kővári', applicant_city='Tokaj', status='new')
Szucs_Zoltan = Applicant.create(first_name='Zoltán', last_name='Szűcs', applicant_city='Eger', status='new')
Toth_Lajos = Applicant.create(first_name='Lajos', last_name='Tóth', applicant_city='Miskolc', status='new')
Lompos_Ferenc = Applicant.create(first_name='Ferenc', last_name='Lompos', applicant_city='Budapest', status='new')
Pinter_Akos = Applicant.create(first_name='Ákos', last_name='Pintér', applicant_city='Tiszaújváros', status='new')
Egri_Laura = Applicant.create(first_name='Laura', last_name='Egri', applicant_city='Szerencs', status='new')
Pici_Kati = Applicant.create(first_name='Kati', last_name='Pici', applicant_city='Budapest', status='new')
Toth_Kriszti = Applicant.create(first_name='Kriszti', last_name='Tóth', applicant_city='Budapest', status='new')
Varga_Dora = Applicant.create(first_name='Dora', last_name='Varga', applicant_city='Vác', status='new')
Tahin_Nora = Applicant.create(first_name='Nora', last_name='Tahin', applicant_city='Tokaj', status='new')
Molnar_Mari = Applicant.create(first_name='Mari', last_name='Molnár', applicant_city='Eger', status='new')
Toth_Lilla = Applicant.create(first_name='Lilla', last_name='Tóth', applicant_city='Miskolc', status='new')
Lompos_Fanni = Applicant.create(first_name='Fanni', last_name='Lompos', applicant_city='Budapest', status='new')
Pinter_Adri = Applicant.create(first_name='Adri', last_name='Pintér', applicant_city='Tiszaújváros', status='new')
Egri_Agi = Applicant.create(first_name='Agi', last_name='Egri', applicant_city='Szerencs', status='new')
Pap_Mira = Applicant.create(first_name='Mira', last_name='Pap', applicant_city='Budapest', status='new')
Mrszky_Weronika = Applicant.create(first_name='Weronika', last_name='Mrszky', applicant_city='Krakow', status='new')
Zrsky_Magdalena = Applicant.create(first_name='Magdalena', last_name='Zrsky', applicant_city='Krakow', status='new')
Trsky_Lena = Applicant.create(first_name='Lena', last_name='Trsky', applicant_city='Krakow', status='new')
Knilky_Karolina = Applicant.create(first_name='Karolina', last_name='Knilky', applicant_city='Wadowice', status='new')
Zrwzky_Nadia = Applicant.create(first_name='Nadia', last_name='Zrwzky', applicant_city='Zawoja', status='new')
Trwurinsky_Milena = Applicant.create(first_name='Milena', last_name='Trwurinsky',
                                     applicant_city='Katowice', status='new')

# Then update the nearest_school and application_code column
applicants = Applicant.select()
for a in applicants:
    # Generate the closest city
    closest_city = GenerateSchool(a.applicant_city)
    a.applied_school = closest_city.nearest_school
    # Create a new app code
    current_app_code = GenerateAppCode()
    a.applicant_code = current_app_code.application_code
    a.save()
