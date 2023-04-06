import re
import functools


# Exercise 1
# Write a script that inserts an item at a defined index in a list.


def insert_an_item(item, index, li):
    li.insert(index, item)
    return li


print(insert_an_item(5, 2, [1, 2, 3, 4]))

# Exercise 2
# Write a script that counts the number of spaces in a string.
print("To be or not to be".count(" "))

# Exercise 3
# Write a script that calculates the number of upper case letters and lower case letters in a string.
input_string = input("Input the string: ")
print(
    f"The number of the uppercase letters in {input_string} is {len(list(filter(lambda e: re.compile(r'[A-Z]+').findall(e), [*input_string])))}")
print(
    f"The number of the lowercase letters in {input_string} is {len(list(filter(lambda e: re.compile(r'[a-z]+').findall(e), [*input_string])))}")


# Exercise 4
# Write a function to find the sum of an array without using the built-in function:
def custom_sum(n):
    s = 0
    for i in n:
        s += i
    return s


print(custom_sum([1, 5, 4, 2]))


# Exercise 5
# Write a function to find the max number in a list
def custom_max(li):
    result = li[0]
    for i in li:
        if i > result:
            result = i
    return result


print(custom_max([1, 2, 3, 4, 2, 3, 0]))


# Exercise 6
# Write a function that returns factorial of a number
def custom_fact(n):
    result = 1
    for i in range(n):
        result = result * (i + 1)
    return result


print(custom_fact(4))


# Exercise 7
# Write a function that counts an element in a list (without using the count method):
def custom_count_elements(li, e):
    counter = 0
    for i in li:
        if i == e:
            counter += 1
    return counter


print(custom_count_elements(['a', 'a', 't', 'o'], 'a'))


# Exercise 8
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:
def custom_l2(li):
    li_sum = 0
    for i in li:
        li_sum += i ** 2
    return round(li_sum ** 0.5)


print(custom_l2([1, 2, 2]))


# Exercise 9
# Write a function to find if an array is monotonic (sorted either ascending of descending)


def is_monotonic(input_data):
    flag = functools.reduce(
        lambda x, y: [y, x[1] + 1, x[2]] if x[0] > y else [y, x[1], x[2] + 1] if x[0] < y else [y, x[1] + 1, x[2] + 1],
        input_data, [input_data[0], 0, 0])
    return True if flag[1] == len(input_data) or flag[2] == len(input_data) else False


print(is_monotonic([7, 6, 5, 5, 2, 0]))
print(is_monotonic([2, 3, 3, 3]))
print(is_monotonic([1, 2, 0, 4]))


# Exercise 10
# Write a function that prints the longest word in a list.

def the_longest(li):
    print(sorted(li, key=lambda e: len(e))[-1])


the_longest(['a', 'aaa', 'dsfsfd', 'sdsaewrwes', 'd'])


# Exercise 11
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

def separate_lists(li):
    return list(filter(lambda e: e.isalpha(), li)), list(filter(lambda e: e.isnumeric(), li))


print(separate_lists(['a', 'dsf', '43', 'sdsd', '1', 'sadaddaAssasd', '10', 's']))


# Exercise 12
# Write a function to check if a string is a palindrome:

def is_palindrome(word):
    return True if word == ''.join([*word][::-1]) else False


print(is_palindrome('radar'))
print(is_palindrome('John'))


# Exercise 13
# Write a function that returns the amount of words in a sentence with length > k:

def length_custom_counter(sentence, k):
    return len(list(filter(lambda e: len(e) > k, sentence.split())))


print(length_custom_counter('Do or do not there is no try', 2))


# Exercise 14
# Write a function that returns the average value in a dictionary (assume the values are numeric):

def dict_average(input_data):
    return round(sum(input_data.values()) / len(input_data))


print(dict_average({'a': 1, 'b': 2, 'c': 8, 'd': 1}))


# Exercise 15
# Write a function that returns common divisors of 2 numbers:

def common_div(x, y):
    divisors = []
    for i in range(2, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            divisors.append(i)
    return divisors


print(common_div(10, 20))


# Exercise 16
# Write a function that test if a number is prime:

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(11))
print(is_prime(6))


# Exercise 17
# Write a function that prints elements of a list if the index and the value are even:

def weird_print(li):
    print([*enumerate(li)], [*enumerate(li)][0][1])
    print(list(filter(lambda e: e[0] % 2 == 0 and e[1] % 2 == 0, [*enumerate(li)])))


weird_print([1, 2, 2, 3, 4, 5])


# Exercise 18
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

def type_count(**args):
    print(args, list(args.values()))
    types = {}
    for i in list(args.values()):
        if str(type(i)) in types.keys():
            types[str(type(i))] += 1
        else:
            types[str(type(i))] = 1
    return {e[e.index("'") + 1:-2]: value for e, value in types.items()}


print(type_count(a=1, b='string', c=1.0, d=True, e=False))


# Exercise 19
# Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.

def custom_split(line, sep=" "):
    result = []
    for i in range(len(line)):
        if i > 0:
            if line[i] == sep:
                result.append("")
            else:
                result[-1] += line[i]
        else:
            result.append(line[i])
    return result


print(custom_split("To be or not to be"))

# Exercise 20
# Convert a string into password format.
print("*" * len("mypassword"))
