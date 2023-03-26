import random

s = input("Enter a string. The string must be 10 characters long: ")
if len(s) < 10:
    print("string not long enough")
elif len(s) > 10:
    print("string too long")
for i in range(0,len(s)+1):
    print(s[0:i])
print("Here's the bonus (the string shuiffled with the whitespaces removed):", ''.join(random.sample(s,len(s))).replace(' ', ''))