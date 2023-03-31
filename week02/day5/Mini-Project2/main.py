import random

words_list = [
    'correction',
    'childish',
    'beach',
    'python',
    'assertive',
    'interference',
    'complete',
    'share',
    'creditcard',
    'rush',
    'south'
]

body_parts = [
    'head',
    'body',
    'left arm',
    'right arm',
    'left leg',
    'right leg'
][::-1]
body = []
guessed = []
typed = []

word = random.choice(words_list)


def update_word(current_word, current_guessed):
    print("".join(map(lambda e: e if e in current_guessed else '*', [*current_word])))


while len(body_parts) > 0:
    update_word(word, guessed)
    if len(set(word)) == len(guessed):
        print("You're the winner!")
        break
    while True:
        current_letter = input("Guess a letter: ").lower()
        if not current_letter.isalpha():
            print("You need to choose a letter! Try again")
        elif current_letter in typed:
            print("You tried this letter before! Try again")
        else:
            typed.append(current_letter)
            break
    if current_letter in word:
        guessed.append(current_letter)
    else:
        body.append(body_parts.pop())
        print("The following body parts are already on the gallows:", ", ".join(body))
else:
    print("I'm sorry, but you've lost! All six body parts are on the gallows")
