# Exercise 1 : What Are You Learning ?
import random
import functools

def display_message(*skills):
    print("We study", ", ".join(skills))


display_message('Python', 'Django', 'JavaScript', 'React')


# Exercise 2: What’s Your Favorite Book ?
def favorite_book(title):
    print("One of my favorite books is", title)


for item in ['The Game of Logic', 'Tiger! Tiger!', 'The Sirens of Titan']:
    favorite_book(item)


# Exercise 3 : Some Geography
def describe_city(city, country = 'Israel'):
    print(f"{city} is in {country}")


describe_city('Reykjavik', 'Iceland')
describe_city('Tel Aviv')


# Exercise 4 : Random
def comparator(n = 0):
    m = random.randint(1, 100)
    if n == m:
        print("A success message")
    else:
        print(f"A fail message, and the numbers are {n} and {m}")


comparator(1)
comparator(2)


# Exercise 5 : Let’s Create Some Personalized Shirts !
def make_shirt(size = 'large', message = 'I love Python'):
    print(f"The size of the shirt is {size} and the text is {message}")


make_shirt("small", "I love JavaScript")
make_shirt()
make_shirt("medium")
make_shirt(message="I love JavaScript")
# Bonus 8
content = ["xlarge", "I prefer C#"]
make_shirt(*content)


# Exercise 6 : Magicians …
def show_magicians(names):
    for name in names:
        print(name)


def make_great(names):
    return list(map(lambda e: 'the Great '+e, names))


magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
show_magicians(magician_names)
magician_names = make_great(magician_names)
show_magicians(magician_names)


# Exercise 7 : Temperature Advice
def get_random_temp(season):
    if season == "winter":
        min_temperature = -10
        max_temperature = 16
    elif season == "spring":
        min_temperature = 5
        max_temperature = 24
    elif season == "summer":
        min_temperature = 24
        max_temperature = 40
    else:
        min_temperature = 0
        max_temperature = 24

    return random.randint(min_temperature, max_temperature)


def main():
    current_season = input("Enter the season (summer, autumn, winter, spring) ")
    current_temperature = get_random_temp(current_season)
    print(f"The temperature right now is {current_temperature} degrees Celsius.")
    if current_temperature > 31:
        print("It's really hot today")
    elif current_temperature > 23:
        print("What a nice weather!")
    elif current_temperature > 16:
        print("The best weather for hiking")
    elif current_temperature >= 0:
        print("Quite chilly! Don’t forget your coat")
    else:
        print("Brrr, that’s freezing! Wear some extra layers today")


main()


# Exercise 7 Bonuses 5 and 6
seasons = ['winter', 'spring', 'summer', 'autumn']
temperature_breakpoints = [0, 16, 24, 32]

def get_random_precise_temperature(season):
    temperatures = [[-10, 16], [5, 24], [24, 40], [0, 24]]
    return random.uniform(*temperatures[seasons.index(season)])


def main_precise():
    messages = [
        "Quite chilly! Don’t forget your coat",
        "The best weather for hiking",
        "What a nice weather!",
        "It's really hot today",
        "Brrr, that’s freezing! Wear some extra layers today"
    ]
    month = int(input("Enter the month (1-12) "))
    if month < 3:
        current_season = seasons[0]
    elif month < 6:
        current_season = seasons[1]
    elif month < 9:
        current_season = seasons[2]
    elif month < 12:
        current_season = seasons[3]
    else:
        current_season = seasons[0]
    current_temperature = get_random_temp(current_season)
    message = functools.reduce(lambda a, e: messages[e[0]] if e[1] <  current_temperature else a, enumerate(temperature_breakpoints), messages[-1])
    print(f"The temperature right now is {current_temperature} degrees Celsius.\n{message}")


main_precise()
