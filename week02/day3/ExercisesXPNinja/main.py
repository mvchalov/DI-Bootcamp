# Exercise 1 : Cars
indata = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
cars = indata.split(", ")
print(f"There are {len(cars)} manufacturers/companies are in the list.")
print(sorted(cars)[::-1])
print(len([item for item in cars if 'o' in item]))
print(len([item for item in cars if 'i' not in item]))
# Bonus 6
cars = [cars[3]] + cars + [cars[1]]
cars = list(set(cars))
print(", ".join(cars)+".", f"The list has {len(cars)} items.")
# Bonus 7
print("Sorted first:", list(map(lambda e: "".join([*e][::-1]), sorted(cars))))
print("Reversed first:", sorted(list(map(lambda e: "".join([*e][::-1]), cars))))