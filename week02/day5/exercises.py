import functools

print(functools.reduce(lambda a, e: a if a > e else e, input_data))