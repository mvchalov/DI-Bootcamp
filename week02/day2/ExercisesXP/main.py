# Exercise 1 : Set
my_fav_numbers = {1, 2, 3, 4, 5}
my_fav_numbers.add(7)
last_num = 9
my_fav_numbers.add(last_num)
my_fav_numbers.difference_update({last_num})
friend_fav_numbers = {11, 12, 13}
all_the_numbers = my_fav_numbers.union(friend_fav_numbers)
print(all_the_numbers)

# Exercise 2: Tuple
# It's impossible, because Tuples are immutable sequences
my_tuple = 1, 2, 3
print(my_tuple)

# Exercise 3: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket = list(["Apples"]+basket)
basket_size = len(basket)
basket = []
print(basket, "This basket has", basket_size, 'size once')

# Exercise 4: Floats
# 1: Float is one of the primitive data types in Python, which represent float numbers, such as 1.1234
# 2: Floats can be also represented as a list of their integer part and decimal part,
# or by all the numbers and the position of the decimal point
# 3:
a = [1.5]
while a[len(a)-1] < 5:
    a.append(a[len(a)-1]+.5)
print(a)

# Exercise 5: For Loop
for i in range(1, 21):
    print(i)
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Exercise 6 : While Loop
my_name = "Max"
your_name = ""
while your_name != my_name:
    your_name = input("Enter your name (until your name is Max): ")

# Exercise 7: Favorite Fruits
favorite_fruits = input("Enter your favorite fruits (separated by whitespaces): ").split(" ")
new_fruit = input("Enter the fruit: ")
if new_fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")

# Exercise 8: Who Ordered A Pizza ?
pizza_toppings = []
pizza_topping = ""
while pizza_topping != "quit":
    if pizza_topping != "":
        pizza_toppings.append(pizza_topping)
        print(f"You've added {pizza_topping} to your pizza")
    pizza_topping = input("Enter the topping one by one separated by Enter (type 'quit' to finish): ")
print("Your pizza {}costs {}".format("includes " + ", ".join(pizza_toppings)+" and " if len(pizza_toppings) > 0 else "", 10 + len(pizza_toppings) * 2.5))

# Exercise 9: Cinemax
family_ages = list(map(lambda e: int(e) if e.isdigit() else 0, input("Enter the ages, separated by whitespace ").split(" ")))
ticket_cost = 0
for e in family_ages:
    if e > 2:
        if e > 12:
            ticket_cost += 15
        else:
            ticket_cost += 10
print(f"The total cost of tickets is {ticket_cost}")

# Exercise 10 : Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
for e in sandwich_orders:
    finished_sandwiches.append(e)
    print(f"I made you a {e}")
sandwich_orders = []
print(f"Orders: {sandwich_orders}\nFinished sandwiches: {finished_sandwiches}")

# Exercise 11 : Sandwich Orders#2
absent_ingredient = "Pastrami"
sandwich_orders_new = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
for x in range(3):
    sandwich_orders_new.append([i for i in sandwich_orders_new if absent_ingredient in i][0])
print("Now the deli has run out of pastrami")
while absent_ingredient in sandwich_orders_new[-1]:
    sandwich_orders_new.pop()
finished_sandwiches = []
for e in sandwich_orders_new:
    finished_sandwiches.append(e)
    print(f"I made you a {e}")
sandwich_orders = []
print(f"Orders: {sandwich_orders_new}\nFinished sandwiches: {finished_sandwiches}")