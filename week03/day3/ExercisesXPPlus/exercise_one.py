# Exercise 1: Import
import func as fn
import random
import string
import datetime
from faker import Faker
from faker.providers import DynamicProvider


fn.custom_add(5, 10)

# Exercise 2: Random Module
for i in range(42):
    fn.random_check(54)

# Exercise 3: String Module
s = "".join(chr(random.choice([random.randint(97, 122), random.randint(65, 90)])) for i in range(5))
s2 = "".join(random.choice([*string.ascii_letters]) for i in range(5))

print(s+'\n'+s2)

# Exercise 4 : Current Date


def show_curr_date():
    print(datetime.date.today().strftime("%d %B %Y"))


show_curr_date()


# Exercise 5 : Amount Of Time Left Until


def until_new_year():
    print((datetime.date(int(datetime.date.today().strftime("%Y"))+1, 1, 1) - datetime.date.today()).days, "days until the new year")


until_new_year()


# Exercise 6 : Birthday And Minutes
def life_in_minutes(*birthday):
    print(round((datetime.date.today() - datetime.date(*birthday)).total_seconds() / 60), "minutes of life")


life_in_minutes(2023, 4, 3)


# Exercise 7 : Upcoming Holiday
# show_curr_date() is already written
def until_holiday():
    holidays = [
        [2023, 4, 6],
        [2023, 4, 26]
    ]
    for holiday in holidays:
        print(datetime.date(*holiday))
        if datetime.date(*holiday) > datetime.date.today():
            print("The next holiday is in", datetime.date(*holiday) - datetime.date.today(), "from now")
            break


until_holiday()


# Exercise 8 : How Old Are You On Jupiter?
def convert_age(age, planet):
    earth_year = 365.25
    planet_corrections = {
        'Earth':    earth_year,
        'Mercury':  earth_year * 0.2408467,
        'Venus':    earth_year * 0.61519726,
        'Mars':     earth_year * 1.8808158,
        'Jupiter':  earth_year * 11.862615,
        'Saturn':   earth_year * 29.447498,
        'Uranus':   earth_year * 84.016846,
        'Neptune':  earth_year * 164.79132
    }
    return round(age / 60 / 60 / 24 / planet_corrections[planet], 2)


print(convert_age(1000000000, 'Earth'))
print(convert_age(1000000000, 'Mercury'))
print(convert_age(1000000000, 'Venus'))
print(convert_age(1000000000, 'Mars'))
print(convert_age(1000000000, 'Jupiter'))
print(convert_age(1000000000, 'Saturn'))
print(convert_age(1000000000, 'Uranus'))
print(convert_age(1000000000, 'Neptune'))


# Exercise 9 : Faker Module
def add_user(user_list):
    fake = Faker()
    language_codes_provider = DynamicProvider(
        provider_name="language_code",
        elements=["en", "de", "ru", "it", "he"]
    )
    fake.add_provider(language_codes_provider)

    new_user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    user_list.append(new_user)


users = []
languages = {
    'en': 'English',
    'de': 'German',
    'ru': 'Russian',
    'it': 'Italian',
    'he': 'Hebrew'
}
for i in range(10):
    add_user(users)
for item in users:
    print('—' * 50)
    print(f"Name: {item['name']}")
    print(f"Address: {item['address']}")
    print(f"Language: {languages[item['language_code']]}")
