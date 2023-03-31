# Mini-Project - Tic Tac Toe
import functools

players = ['X', 'O']


def display_score(score):
    decor = "* "
    for i in range(3):
        print(decor+' ', " | ".join(map(lambda e: ' '.join(e), score[i])), ' '+"".join(reversed([*decor])))
        if i < 2:
            print(decor, "---|---|---", "".join(reversed([*decor])))


def display_board(score):
    print("TIC TAC TOE")
    print('*' * 17)
    display_score(score)
    print('*' * 17)


def is_winner(current_score):
    combinations = list("".join(functools.reduce(lambda a, e: a+e, current_score[i])) for i in range(3))
    combinations += list("".join(functools.reduce(lambda a, e: a + e, [current_score[j][i] for j in range(3)])) for i in range(3))
    combinations += ["".join(list(functools.reduce(lambda a, e: a + e, list(current_score[i][i] for i in range(3))+[])))]
    combinations += ["".join(list(functools.reduce(lambda a, e: a + e, list(current_score[2-i][i] for i in range(3)) + [])))]
    if players[0]*3 in combinations:
        print("Player One wins")
    elif players[1]*3 in combinations:
        print("Player Two wins")
    else:
        return False
    return True


def turn(current_player, current_score):
    print("Player", players[current_player % 2]+"'s turn...")
    while True:
        y = input("Enter row: ")
        x = input("Enter column: ")
        if y.isdigit() and x.isdigit() and 0 < int(x) < 4 and 0 < int(y) < 4 and current_score[int(y) - 1][int(x) - 1] == [' ']:
            current_score[int(y) - 1][int(x) - 1] = [players[current_player % 2]]
            break
        else:
            print("Your input is incorrect. Please, type again")
    display_board(current_score)
    if not is_winner(current_score):
        turn(current_player + 1, current_score)


def game():
    print("Welcome to TIC TAC TOE!\n")
    score = [[[' '] for _ in range(3)] for __ in range(3)]
    display_board(score)
    turn(0, score)


game()
