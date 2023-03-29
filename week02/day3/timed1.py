import functools

num = int(input("Enter the number: "))
divisors = []
for i in range(1, num):
    if num % i == 0:
        divisors.append(i)
if functools.reduce(lambda a, e: a + e, divisors, 0) == num:
    print('True')
else:
    print('False')
