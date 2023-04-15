from game import Game


class RockPaperScissors:

    def __init__(self):
        self.main()

    def get_user_menu_choice(self):
        print('┌' + '─' * 23 + '┐')
        print('│ Play a new game   (p) │')
        print('├' + '—' * 23 + '┤')
        print('│ Show scores       (s) │')
        print('├' + '—' * 23 + '┤')
        print('│ Quit              (q) │')
        print('└' + '─' * 23 + '┘\n')
        while True:
            user_choice = input("Enter your choice: ").lower()
            if user_choice and user_choice in "psq":
                return user_choice
            else:
                print("Please, enter a valid letter: p, s, q")

    def print_results(self, results):
        print('┌' + '─' * 23 + '┐')  #
        print('│  -> CURRENT SCORE <-  │')
        for key, value in results.items():
            c1 = 0
            c2 = 0
            if len(key) % 2 == 0:
                c1 = 1
            if len(str(value)) % 2 == 0:
                c2 = 1

            print('├' + '—' * 23 + '┤')
            print('│' + ' ' * (int((24 - len(key)) / 2) - c1) + key + ' ' * int((24 - len(key)) / 2) + '│')
            print('│' + ' ' * (int((24 - len(str(value))) / 2) - c2) + str(value) + ' ' * int((24 - len(str(value))) / 2) + '│')
        print('└' + '─' * 23 + '┘')


    def main(self):
        scores = {
            'win': 0,
            'loss': 0,
            'draw': 0
        }
        choices = {
            'r': 'ROCK',
            'p': 'PAPER',
            's': 'SCISSORS'
        }
        while True:
            choice = self.get_user_menu_choice()
            if choice == "q":
                self.print_results(scores)
                break
            elif choice == "s":
                self.print_results(scores)
            else:
                result, users_choice, computers_choice = Game.play()
                scores[result] += 1
                print(f"You played {choices[users_choice]}, computer — {choices[computers_choice]}. It's a {result}!")


game = RockPaperScissors()
