# Daily Challenge: Sorting
# input_data = "without,hello,bag,world".split(",")
input_data = input("Enter a comma separated sequence of words: ").split(",")
print(",".join(sorted(input_data)))
# Using List Comprehension
sorted_part = [min(input_data)]
unsorted_part = [item for item in input_data if item not in sorted_part]
for i in range(len(input_data)-1):
    sorted_part += [min(unsorted_part)]
    unsorted_part = [item for item in unsorted_part if item not in sorted_part]
print(",".join(sorted(sorted_part)))
