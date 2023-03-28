import random

# Exercise 1: Birthday Look-Up
birthday = {
    'Amy':      '1990/11/12',
    'Joy':      '1985/05/17',
    'Dan':      '1988/10/02',
    'Mary':     '1977/06/14',
    'Carol':    '1984/09/29'
}
print("You can look up the birthdays of the people in the list!")
print("Here's the list of persons:", ", ".join(birthday.keys()))

# Exercise 3: Add Your Own Birthday
if input("Would you like to add your birthdate to the list? (y for yes) ").lower() == 'y':
    user_name = input("Enter your name: ")
    if user_name.title() in birthday.keys():
        print("We already know your birthdate!", birthday[user_name.title()])
    else:
        user_birthdate = input("Enter your birthdate (YYYY/MM/DD): ")
        birthday[user_name.title()] = user_birthdate

person = input("Enter the person's name: ")
if person.title() in birthday.keys():
    print(f"According to our list, {person.title()} has born on {birthday[person.title()]}")
else:
    print("Sorry, we don’t have the birthday information for", person)


# Exercise 2: Birthdays Advanced
# Done above!


# Exercise 4: Fruit Shop
# 1
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
item_adjectives = [
    "perfect",
    "tasty",
    "magical",
    "fresh"
]
cost_phrases = [
    "is as cheap as {}₪ per kilo",
    "sells for no more than {}₪ per fruit",
    "costs just {}₪ for one 1kg",
    "can be bought for as little as {}₪ per item"
]
random.shuffle(cost_phrases)
random.shuffle(item_adjectives)
sentence = "; ".join(list(" ".join(e) for e in list(zip(item_adjectives, items.keys(), cost_phrases))))
sentence = sentence[0].upper() + sentence[1:]
print(sentence.format(*items.values()))

# 2
stock = [10, 5, 24, 1]
new_items = {}
whole_sum = 0;
for key in items.keys():
    whole_sum += items[key] * stock[len(new_items)]
    new_items[key] = {'price': items[key], 'stock': stock[len(new_items)]}
print("-> You need to spend", whole_sum, "to buy everything in stock.")
