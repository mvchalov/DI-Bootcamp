# All You Need To Know About Functions: Function Exercise
def highest_even(li):
    return sorted(filter(lambda e: e % 2 == 0, li))[-1]


print(highest_even([2, 10, 3, 4, 11, 8]))
print(highest_even([1, -10, -53, -12, 2, 0]))


