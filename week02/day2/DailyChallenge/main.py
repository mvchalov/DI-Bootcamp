# Challenge 1
number = int(input("Enter the number: "))
length = int(input("Enter the length: "))
result = []
for i in range(length):
    result.append(number*(i+1))
print(result)

# Challenge 2
user_string = input("Enter the string: ")
result_string = user_string[0]
for index, value in enumerate(user_string):
    if index > 0 and value != result_string[-1]:
        result_string += value
print(result_string)
