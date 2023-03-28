import string

rules = input('Enter the cipher code, for example, <<< means to shift left 3 times: ')
counter = len(rules)
if '<' in rules:
    counter = -1*counter


def encryptor(word, rule):
    cipher = ''
    for char in word:
        if char.islower():
            cipher += chr((ord(char) - 97 + rule) % 26 + 97)
        elif char.isupper():
            cipher += chr((ord(char) - 65 + rule) % 26 + 65)
        else:
            cipher += char
    return cipher


def decryptor(word, rule):
    decipher = ''
    for char in word:
        if char.islower():
            decipher += chr((ord(char) - 97 - rule) % 26 + 97)
        elif char.isupper():
            decipher += chr((ord(char) - 65 - rule) % 26 + 65)
        else:
            decipher += char
    return decipher


text = input("Enter the word for encryption or / and decryption: ")
if input("Would you like to encrypt it? y means yes: ") == 'y':
    print("If this text has to be encrypted:", encryptor(text, counter))
if input("Would you like to decrypt it? y means yes: ") == 'y':
    print("If this text has to be decrypted:", decryptor(text, counter))