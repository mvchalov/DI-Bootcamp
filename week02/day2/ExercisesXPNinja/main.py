import random
from functools import reduce


# Exercise 1: Formula
def formula(c, h, d):
    return ((2*c*d)/h)**(1/2)


c_real = 50
h_real = 30
d_real = input("Enter comma-separated string of numbers: ").split(",")
formula_results = []
for e in d_real:
    formula_results.append(str(int(formula(c_real, h_real, int(e)))))
print(','.join(formula_results))


# Exercise 2 : List Of Integers

# Solution using built-in functions:
def standard_solution(list_of_numbers):
    print("The list of numbers – printed in a single line:", list_of_numbers)
    print("The list of numbers – sorted in descending order", sorted(list_of_numbers, reverse=True))
    print("The sum of all the numbers:", reduce(lambda a, b: a + b, list_of_numbers, 0))
    print("A list containing the first and the last numbers:", [list_of_numbers[0], list_of_numbers[-1]])
    print("A list of all the numbers greater than 50:", list(filter(lambda e: e > 50, list_of_numbers)))
    print("A list of all the numbers smaller than 10:", list(filter(lambda e: e < 10, list_of_numbers)))
    print("A list of all the numbers squared:", list(map(lambda e: e * e, list_of_numbers)))
    print("The numbers without any duplicates and the length of the list:", set(list_of_numbers),
          len(set(list_of_numbers)))
    print("The average of all the numbers:", int(reduce(lambda a, b: a + b, list_of_numbers, 0) / len(list_of_numbers)))
    print("The largest number:", max(list_of_numbers))
    print("The smallest number", min(list_of_numbers))


# Bonus (11): Find the sum, average, largest and smallest number without using built-in functions
def custom_solution(list_of_numbers):
    min_of_list = list_of_numbers[0]
    max_of_list = list_of_numbers[0]
    sum_of_list = 0
    for n in list_of_numbers:
        if n < min_of_list:
            min_of_list = n
        if n > max_of_list:
            max_of_list = n
        sum_of_list += n
    print("The sum", sum_of_list)
    print("The average number", int(sum_of_list / len(list_of_numbers)))
    print("The largest number", max_of_list)
    print("The smallest number", min_of_list)


# Predefined input
# input_list = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7, 5, 5]

# Input in a string
# input_list = list(map(lambda e: int(e), input("Enter comma-space-separated list of 10 integers: ").split(", ")))

# Bonus 12: input number by number
# input_list = []
# while len(input_list) < 10:
#     current_number = input("Enter a number between -100 and 100: ")
#     if current_number.isdigit():
#         input_list.append(int(current_number))

# Bonus 13: generate 10 random integers between -100 and 100
# input_list = random.sample(range(-100, 101), 10)
# print(input_list)

# Bonus 14: Instead of always generating 10 integers, let the amount of integers also be random
list_length = random.randint(50, 202)
input_list = random.sample(range(-100, 101), list_length)
# print(input_list)

# 15.Bonus: Will the code work when the number of random numbers is not equal to 10?
# Answer: Yes!
standard_solution(input_list)
custom_solution(input_list)


# Exercise 3: Working On A Paragraph
paragraph = """Python is an incredibly versatile and powerful programming language with numerous advantages. Firstly, its syntax is designed to be easy to read and write, making it accessible to both novice and experienced programmers alike. Python is also an interpreted language, which means that code can be executed immediately without the need for time-consuming compilation. Additionally, Python has a vast array of libraries and frameworks that can be used to simplify complex tasks and accelerate development. This means that Python can be used for a wide range of applications, including web development, scientific computing, data analysis, and machine learning. Moreover, Python's popularity has led to a thriving community of developers who contribute to open-source libraries and tools, ensuring that the language is continually evolving and improving. Overall, Python's simplicity, versatility, and community make it an excellent choice for both beginners and experienced programmers."""
total_words = len(paragraph.split())
unique_words = len(set("".join(filter(lambda e: e if e.isalnum() or e.isspace() else None, [*paragraph])).lower().split()))
print("This paragraph contains {} characters, {} sentences and {} words.".format(len(paragraph), len(paragraph.split('.')), total_words))
print("There are {} unique words in this paragraph".format(unique_words))
# Bonuses
print("There are {} non-whitespace characters".format(len("".join(paragraph.split()))))
print("The average amount of words per sentence is", int(total_words/len(paragraph.split('.'))))
print("The amount of non-unique words in the paragraph is", total_words - unique_words)


# Exercise 4
string_given = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.".split()
# string_given = input("Enter the string: ").split()
frequency_of_words = {}
for e in string_given:
    if e in frequency_of_words:
        frequency_of_words[e] += 1
    else:
        frequency_of_words[e] = 1
for key, value in frequency_of_words.items():
    print(key+':', value)
