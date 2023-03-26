#For example,
#my_name = "Frank"  this line creates a name variable type: string
#print("My name is {}".format(my_name))

cars = 100
# type int
space_in_a_car = 4.0
#type float
drivers = 30
# type int
passengers = 90
# type int
cars_not_driven = cars - drivers
# type int
cars_driven = drivers
# type int
carpool_capacity = cars_driven * space_in_a_car
#type float
average_passengers_per_car = passengers / cars_driven
#type float

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")

