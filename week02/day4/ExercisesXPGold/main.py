import functools
import random
from decimal import Decimal

from datetime import date

# Exercise 1 : When Will I Retire ?


def get_age(year, month, day):
    birthday = date(year, month, day)
    today = date.today()
    return int((today-birthday).total_seconds() / (365.2425 * 24 * 3600))


def can_retire(gender, date_of_birth):
    rules = {
        'f': 62,
        "m": 67
    }
    return get_age(*date_of_birth) >= rules[gender] or False


users_gender = input("Enter your gender (m or f): ")
users_birthdate = input("Enter your date of birth in the form of “yyyy/mm/dd: ")

if can_retire(users_gender, list(map(lambda e: int(e), (users_birthdate.split("/"))))):
    print("Congratulations! You can definitely retire now")
else:
    print("Your future is ahead of you! Work hard")


# Exercise 2 : Sum
def sum_producer(value):
    result = 0
    for i in range(4):
        result += int(value*(i+1))
    return result


x = input("Enter X: ")
print("The sum is", sum_producer(x))

# Exercise 3 : Double Dice
tries = 100


def throw_dice():
    return random.randint(1, 6)


def throw_until_doubles():
    i = 0
    while True:
        i += 1
        if throw_dice() == throw_dice():
            return i


def main():
    results = []
    for i in range(tries + 1):
        results.append(throw_until_doubles())
    return results


throw_results = functools.reduce(lambda a, e: a + e, main(), 0)
print("Total throws:", throw_results)
print("Average throws to reach doubles:", Decimal(throw_results/tries).quantize(Decimal('1.00')))
