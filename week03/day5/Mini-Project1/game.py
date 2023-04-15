from random import randint


class Game:

    def get_user_item(self):
        while True:
            users_choice = input("Select an item: (r)ock/(p)aper/(s)cissors: ").lower()
            if users_choice and users_choice in "rps":
                return users_choice.lower()
            else:
                print("Please, enter a valid letter: p, s, q")

    def get_computer_item(self):
        return "rps"[randint(0, 2)]

    def get_game_result(self, user_item, computer_item):
        winning_schemes = ["pr", "rs", "sp"]
        results = ["win", "loss", "draw"]
        scheme = user_item + computer_item
        if scheme in winning_schemes:
            return results[0]
        elif "".join([*scheme][::-1]) in winning_schemes:
            return results[1]
        else:
            return results[2]

    @classmethod
    def play(cls):
        user_turn = cls.get_user_item(cls)
        computer_turn = cls.get_computer_item(cls)
        return cls.get_game_result(cls, user_turn, computer_turn), user_turn, computer_turn
