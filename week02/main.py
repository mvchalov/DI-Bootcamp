# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#
#

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

print("Here's the data:")
print(f"There are {cars} cars available.")
print(f"There are only {drivers} drivers available.")
print("There will be {} empty cars today.".format(cars_not_driven))
print("We can transport {} people today.".format(int(carpool_capacity)))
print("We have", int(passengers), "to carpool today.")
print("We need to put about", int(average_passengers_per_car),"in each car.")

#

num = int(input("1-100:"))
a = ''
if num%3==0:
    a+='Fizz'
if num%5==0:
    a+='Buzz'
print(a)

