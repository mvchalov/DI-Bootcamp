input_data = []
for _ in range(5):
    name = input("Name: ")
    age = input("Age: ")
    score = input("Score: ")
    input_data.append((name, age, score))
print(sorted(input_data, key=lambda e: (e[0], int(e[1]), int(e[2]))))
