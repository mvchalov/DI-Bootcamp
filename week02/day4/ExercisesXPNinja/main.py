# Exercise 1 : What’s Your Name ?
def get_full_name(first_name, last_name, middle_name=None):
    parts = [item for item in [first_name, middle_name, last_name] if item is not None]
    return " ".join(part.title() for part in parts)


print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))

# Exercise 2 : From English To Morse
morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '/'
}


def to_morse_code(letter):
    return morse_code[letter]


input_string = input("Enter string to encode (only letters, numbers and whitespaces are allowed): ")
result = [to_morse_code(i) for i in input_string.upper()]
print(" ".join(result))


# Exercise 3 : Box Of Stars
def box_printer(input_data):
    width = max(len(e) for e in input_data)
    print('*' * (width + 4))
    for i in range(len(input_data)):
        print('*', input_data[i] + ' ' * (width - len(input_data[i])), '*')
    print('*' * (width + 4))


strings = []
while True:
    input_string = input("Enter your string (type q for quit): ")
    if input_string == 'q':
        break
    else:
        strings.append(input_string)

box_printer(strings)

# Exercise 4
# It sorts the list in ascending order
