# Functions: Exercise
def calculation(a, b):
    return a+b, a-b


print(calculation(5,3))

# Lambda, Map, Reduce & Filter Functions: Exercise
people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
print("\n".join(map(lambda e: 'Hello '+e, filter(lambda e: len(e) < 5, people))))
