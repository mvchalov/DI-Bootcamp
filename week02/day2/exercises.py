# Sequences, List, Sets, Tuple

# Exercise 1 (without handling the ValueError)
list1 = [5, 10, 15, 20, 25, 50, 20]
list1[list1.index(20)] = 200
print(list1)

# Exercise 2
a_tuple = (10, 20, 30, 40)
a, b, c, d = a_tuple
print(a, b, c, d)

# Exercise 3
my_set = set()
my_set.add("Element1")
my_set.add("Element2")
my_set.add("Element3")
my_set.add("Element2")
print(my_set)
this_set = {"do", "it", "again", "and", "again"}
print(this_set)
# just for fun
print(sorted(this_set))


# Loops

# Exercise 1
b = []
a = int(input("Enter a number: "))
for i in range(1, a+1):
    b.append(i*a)
print(b)

# Exercise 2
i = 1
while i < 11:
    print(i)
    i += 1