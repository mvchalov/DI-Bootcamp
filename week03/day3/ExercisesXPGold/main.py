import random
import re
import string
# Exercise 1 : Regular Expression #1
input_string = input("Enter a string: ")
print(''.join(re.findall(r'\d', input_string)))

# Exercise 2 : Regular Expression #2
username = input("Enter your name: ")
flag = True
if all(map(lambda e: re.match(r'[a-z A-Z]', e), [*username])):
    parsed = username.split()
    if len(parsed) == 2:
        if re.match(r'[A-Z]',parsed[0][0]) and re.match(r'[A-Z]', parsed[1][0]):
            if not re.fullmatch(r'[a-z]+', parsed[0][1:]) or not re.fullmatch(r'[a-z]+', parsed[1][1:]):
                flag = False
        else:
            flag = False
    else:
        flag = False
else:
    flag = False
if flag:
    print("Your name is correct!")
else:
    print("Sorry, your input is not a valid name")


# Exercise 3: Python Password Generator
def generate_password(length):
    password_pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()_+|}{":?><,./;\'[\]\\=-])(?!.*\s)'
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password_candidate = ''.join(random.choices(characters, k=length))
        if re.match(password_pattern, password_candidate):
            break
    return password_candidate


def test_password(password_to_check):
    counter = 0
    if re.search(r'\d', password_to_check) is not None:
        counter += 1
    if re.search(r'[a-z]', password_to_check) is not None:
        counter += 1
    if re.search(r'[A-Z]', password_to_check) is not None:
        counter += 1
    if re.search(r'[!@#$%^&*()_+|}{":?><,./;\'[\]\\=-]', password_to_check) is not None:
        counter += 1
    if 31 > len(password_to_check) > 5:
        counter += 1
    return True if counter == 5 else False


while True:
    password_length = input("Enter the password length (between 6 and 30 characters): ")
    if password_length.isnumeric():
        if 31 > int(password_length) > 5:
            break
print("Here's your password:", generate_password(int(password_length)), "\nPlease, keep the password in a safe place")

for _ in range(100):
    tryout = generate_password(random.randint(6, 30))
    print(f"Test password {tryout} is checked and {'flawless' if test_password(tryout) else 'horrible'}!")