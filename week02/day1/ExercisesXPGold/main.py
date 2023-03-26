# Exercise 1 : Hello World-I Love Python
print("Hello world\n"*5+"I love python\n"*5)

# Exercise 2 : What Is The Season ?
month = int(input("Input a month: "))
if month == 12 or month < 3:
    print("Winter")
elif month > 8:
    print("Autumn")
elif month > 5:
    print("Summer")
else:
    print("Spring")