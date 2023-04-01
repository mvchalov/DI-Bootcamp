# Exercise 1
# Part 1
def pyramid(n):
    for i in range(n):
        print(' '*int((2*n-1 - 2*i - 1)/2) + '*'*(2*i+1))


pyramid(3)
pyramid(5)
pyramid(19)


# Part 2
def triangle(n):
    for i in range(n):
        print(' '*(n-1-i)+'*'*(i+1))


triangle(5)
triangle(11)


# Part 3
def triangle2(n):
    for i in range(n):
        print('*'*(i+1)+' '*(n-1-i))
    for i in reversed(range(n)):
        print(' '*(n-1-i)+'*'*(i+1))


triangle2(5)
triangle2(11)


# Exercise 2
# The following code sort the list in ascending order using bubble sort algorithm
my_list = [2, 24, 12, 354, 233]             # list declaration
for i in range(len(my_list) - 1):           # loops length of my_list - 1 times, starting from 0
    minimum = i                             # initializes a variable called minimum with value i
    for j in range( i + 1, len(my_list)):   # loops from i+1 to length of my_list
        if(my_list[j] < my_list[minimum]):  # checks if the current item of the list is smaller than the current minimum, set before the beginning of the loop
            minimum = j                     # if it is smaller, then set minimum to the current index
            if(minimum != i):               # check if the new minimum is not egual to the initial minimum
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i] # if it is not equal to the initial minimum (i), then swaps the initial element and the current minimum element by their places
print(my_list)  # prints the sorted list