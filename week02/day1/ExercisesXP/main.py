# Exercise 1 : Hello World
print('Hello world\n'*5)

# Exercise 2 : Some Math
print((99**3)*8, '\n')

# Exercise 3 : What Is The Output ?
# 5 < 3
# False
# 3 == 3
# True
# 3 == "3"
# False
# "3" > 3
# TypeError
# "Hello" == "hello"
# False

# Exercise 4 : Your Computer Brand
computer_brand = 'Mac'
print(f"I have a {computer_brand} computer\n")

# Exercise 5 : Your Information
name = 'Max'
age = '42'
shoe_size = '40'
info = f"an interesting sentence about myself is that my name is {name}, I'm {age} and wear {shoe_size} shoe size\n"
print(info)

# Exercise 6 : A & B
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if a > b:
    print('Hello World\n')

# Exercise 7 : Odd Or Even
a = int(input("Enter the number: "))
if a%2==0:
    print('even\n')
else:
    print('odd\n')

# Exercise 8 : What’s Your Name ?
my_name = 'max'
your_name = input("Your name: ").lower()
if my_name == your_name:
    print(f"Are you kidding me, {your_name.title()}! I'm {my_name.title()} too!")
else:
    print(f"Who are you, {your_name.title()}")

# Exercise 9 : Tall Enough To Ride A Roller Coaster
h = int(input("Tell me your height in inches: "))

if h*2.54 > 145:
    print("You're tall enough to ride")
else:
    print("You need to grow some more to ride")