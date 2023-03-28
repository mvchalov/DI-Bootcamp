# Exercise 1 : Convert Lists Into Dictionaries
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(dict(zip(keys, values)))


# Exercise 2 : Cinemax
def calculate_costs(group_of_people):
    total_cost = 0
    for key, value in group_of_people.items():
        ticket_cost = 0
        if value > 2:
            if value > 12:
                ticket_cost += 15
            else:
                ticket_cost += 10
        total_cost += ticket_cost
        print(key, "has to pay", ticket_cost)
    print("The total cost of tickets is", total_cost)


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
calculate_costs(family)
# Bonus
family = {}
while True:
    name = input("Enter a name of a family member. For quit type 0: ")
    if name == '0':
        break
    age = input("How old is this person? ")
    family[name] = int(age)
calculate_costs(family)


# Exercise 3: Zara
brand = {'name': 'Zara',
         'creation_date': 1975,
         'creator_name': 'Amancio Ortega Gaona',
         'type_of_clothes': ['men', 'women', 'children', 'home'],
         'international_competitors': ['Gap', 'H&M', 'Benetton'],
         'number_stores': 7000,
         'major_color': {
            'France': 'blue',
            'Spain': 'red',
            'US': ['pink', 'green']
                        }
         }
brand['number_stores'] = 2
print(f"The brand of {brand['name']} provides clothes for {', '.join(brand['type_of_clothes'])}.")
brand['country_creation'] = 'Spain'
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')
del brand['creation_date']
print("The last international competitor in the list is",brand['international_competitors'][-1])
print("The major colors in the US are:", ', '.join(brand['major_color']['US']))
print("The length of the dictionary is", len(brand))
print("The keys of the dictionary:", brand.keys())
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}
brand.update(more_on_zara)
print(f"The number of stores is {brand['number_stores']} now")


# Exercise 4 : Disney Characters
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
disney_users_B = dict(enumerate(users))
disney_users_A = {key: index for index, key in disney_users_B.items()}
print(disney_users_A)
print(disney_users_B)
disney_users_C = {key: disney_users_A[key] for key in sorted(list(disney_users_A.keys()))}
print(disney_users_C)
# Use a for loop to recreate the 1st result.
disney_users_A = {}
for i in users:
    disney_users_A[i] = users.index(i)
print(disney_users_A)
# Use a for loop to recreate the 2nd result.
disney_users_B = {}
for i in users:
    disney_users_B[users.index(i)] = i
print(disney_users_B)
# Use a method to recreate the 3rd result
# Done already :)
# 4
disney_users_A = list(filter(lambda e: 'i' in e or e[0].lower() in 'mp', users))
counter = range(len(disney_users_A))
print(dict(zip(disney_users_A, counter)))