import random
import string

# Exercise 1: Concatenate Lists
print([1, 2] + ['a', 'b'])

# Exercise 2: Range Of Numbers
for i in range(1500, 2501):
    if i % 5 == 0 or i % 7 == 0:
        print(i)

# Exercise 3: Check The Index
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
your_name = input("Enter your name: ")
if your_name in names:
    print(your_name,"has index",names.index(your_name))

# Exercise 4: Greatest Number
numbers_for_max = []
for i in range(0, 3):
    if i == 0:
        index_formatted = "1st"
    elif i == 1:
        index_formatted = "2nd"
    else:
        index_formatted = "3rd"
    numbers_for_max.append(int(input(f"Input the {index_formatted} number: ")))
print("The greatest number is:", max(numbers_for_max))

# Exercise 5: The Alphabet
vowels = "aoeiu"
for e in string.ascii_lowercase:
    if e in vowels:
        letter_type = "vowel"
    else:
        letter_type = "consonant"
    print(e, "is a", letter_type)

# Exercise 6: Words And Letters
words = []
for i in range(0,7):
    words.append(input("Enter a word: "))
letter = input("Enter a single character: ")
for e in words:
    if letter in e:
        print(f"The index of the letter in the word {e} is {e.index(letter)}")
    else:
        print(f"There's no letter {letter} in the word {e}")

# Exercise 7:
numbers_list = list(range(1,1000001))
print("The min() result is {}, the max() result is {}, the sum() result is {}".format(min(numbers_list), max(numbers_list), sum(numbers_list)))

# Exercise 8 : List And Tuple
# input_string = "34,67,55,33,12,98"
input_string = input("Enter comma-separated numbers: ")
print(input_string.split(","))
print(tuple(input_string.split(",")))

# Exercise 9 : Random Number
while True:
    user_number = 0
    while user_number < 1 or user_number > 9:
        user_number = int(input("Enter a number from 1 to 9 (including): "))
    python_number = random.randint(1, 9)
    if user_number == python_number:
        print("You're the Winner")
    else:
        print("Good luck next time!")

        # Bonus 5
        if input("Would you like to continue guessing this number? (y = yes): ") == 'y':
            while user_number != python_number:
                user_number = int(input("Enter a number from 1 to 9 (including): "))
            print("Finally you have won!")
    # Bonus 6
    if input("------> IF YOU WANT TO PLAY AGAIN, type y! ") != 'y':
        break
