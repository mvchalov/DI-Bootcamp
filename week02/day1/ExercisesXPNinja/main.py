# Exercise 1 : Use The Terminal
# Done

# Exercise 2 : Alias
# Done

# Exercise 3 : Outputs
#     >>> 3 <= 3 < 9
#   True
#     >>> 3 == 3 == 3
#   True
#     >>> bool(0)
#   True
#     >>> bool(5 == "5")
# False
#     >>> bool(4 == 4) == bool("4" == "4")
# True
#     >>> bool(bool(None))
# True
#     x = (1 == True)
# False
#     y = (1 == False)
# False
#     a = True + 4
# 5
#     b = False + 10
# 10
#     print("x is", x)
# appears the string: x is False
#     print("y is", y)
# appears the string: y is False
#     print("a:", a)
# appears the string: a: 5
#     print("b:", b)
# appears the string: b: 10

# Exercise 4 : How Many Characters In A Sentence ?
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.Excepteur sint occaecat cupidatat non proident,sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))

# Exercise 5: Longest Word Without A Specific Character
max_length = 0
while (True):
    a = input("Enter the longest string without the character A (to exit type q): ").upper()
    if len(a) > max_length and a.find('A') == -1:
        max_length = len(a)
        print ("Congratulations! The new recors is set to",max_length)
    if a == 'Q':
        break