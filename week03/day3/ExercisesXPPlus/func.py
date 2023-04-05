import random


def custom_add(n, m):
    result = n + m
    print(result)


def random_check(n):
    if random.randint(1, 100) == n:
        print("It's a match!")
