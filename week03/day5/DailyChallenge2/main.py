# Part 2: Create A Deck Of Cards Class
from itertools import product
from random import shuffle, randint
card_suits = [
    'Hearts',
    'Diamonds',
    'Clubs',
    'Spades'
]
card_values = [
    'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
]


class Card:
    def __init__(self, suit=card_suits[0], value=card_values[0]):
        self.suit = suit
        self.value = value

    def get_the_card(self):
        return self.suit, self.value


class Deck:
    def __init__(self):
        self.deck = [Card(suit, value) for suit, value in product(card_suits, card_values)]

    def shuffle_deck(self):
        shuffle(self.deck)

    def deal_a_card(self):
        chosen_card_idx = randint(0, len(self.deck)-1)
        return self.deck.pop(chosen_card_idx)

    def get_the_deck(self):
        return [card.get_the_card() for card in self.deck]


playing_deck = Deck()
print(playing_deck.get_the_deck())
playing_deck.shuffle_deck()
print("The deck is shuffled!")
print(playing_deck.get_the_deck())
while True:
    choice = input("Would you like to deal a card? (y/n) ")
    if choice.lower() == "y":
        print("This card is dealt:", playing_deck.deal_a_card().get_the_card())
    else:
        break
print(f"The rest of the deck: ({len(playing_deck.deck)} cards left)")
print(playing_deck.get_the_deck())
