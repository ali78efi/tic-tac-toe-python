from functools import wraps
from os import name, system
from time import sleep
import math


def _clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def table_render(table_list):
    # first line
    print("╔══", "═" *
          len(str(table_list[get_size()-1][get_size()-1])), sep="", end="")
    for i in range(len(table_list)-1):
        print("╦══", "═" *
              len(str(table_list[get_size()-1][get_size()-1])), sep="", end="")
    print("╗")

    # middle lines
    for i in range(len(table_list)):
        row = table_list[i]
        print("║", end="")
        for column in row:
            print(" "*(len(str(table_list[get_size()-1][get_size()-1]))-len(str(column))+1), column, " ", "║", sep="", end="")
        print("")
        if i != len(table_list)-1:
            print("╠══", "═" *
                  len(str(table_list[get_size()-1][get_size()-1])), sep="", end="")
            for i in range(len(table_list)-1):
                print(
                    "╬══", "═"*len(str(table_list[get_size()-1][get_size()-1])), sep="", end="")
            print("╣", end="\n")

    # last line
    print("╚══", "═" *
          len(str(table_list[get_size()-1][get_size()-1])), sep="", end="")
    for i in range(len(table_list)-1):
        print("╩══", "═" *
              len(str(table_list[get_size()-1][get_size()-1])), sep="", end="")
    print("╝")


def table_size_memorizing(get_size_func):
    memory = dict({})

    @wraps(get_size_func)
    def inner(*args, **kwargs):
        if "size" not in memory:
            memory["size"] = get_size_func(*args, *kwargs)
        return memory["size"]
    return inner


@table_size_memorizing
def get_size():
    try:
        table_size = int(
            input("enter the size of game table(minimum :3) : ".strip(" ")))
        if table_size < 3:
            table_size = 3
        return table_size
    except:
        return 3


def welcome():
    print("tic tac toe")
    print("author Ali Eftekhari")
    sleep(1.7)
    _clear()
    n1 = input("Player one please enter your name: ").strip(" ")
    n2 = input("Player two please enter your name: ").strip(" ")
    if n1 == "":
        n1 = "Player1"
    if n2 == "":
        n2 = "Player2"
    if n1 == n2:
        n1 += "(1)"
        n2 += "(2)"
    table_size = get_size()
    my_list = []
    for i in range(1, ((table_size*(table_size-1)+1)+1), table_size):
        row = list(range(i, i+table_size))
        my_list.append(row)

    while True:
        _clear()
        table_render(my_list)
        print(n1, n2, sep=" vs ")
        print()
        s = input("enter \"s\" to start: ")
        if s == 's':
            return [n1, n2]


def game_list_render(n):
    game_list = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(" ")
        game_list.append(row)
    return game_list


def calCell(n):
    table_size = get_size()

    row = int(math.ceil(n/table_size))
    column = int(n % table_size)
    if column == 0:
        column = table_size
    return row-1, column-1


def move(turn, name, game_list):
    cell = int(
        input(f"{name}'s turn : enter a cell number (1-{get_size()**2}): ").strip(" "))
    cell_row, cell_column = calCell(cell)
    if game_list[cell_row][cell_column] != 'X' and game_list[cell_row][cell_column] != 'O':
        if turn % 2 == 0:
            game_list[cell_row][cell_column] = "X"
        if turn % 2 == 1:
            game_list[cell_row][cell_column] = "O"
    else:
        turn -= 1
    return turn


def win_check(game_list):
    # rows check
    for row in game_list:
        if row[0] != " " and all(x == row[0] for x in row):
            if row[0] == 'X':
                return 0
            else:
                return 1

    # columns check
    for i in range(get_size()):
        column = []
        for j in range(get_size()):
            column.append(game_list[j][i])
        if column[0] != " " and all(x == column[0] for x in column):
            if column[0] == 'X':
                return 0
            else:
                return 1

    # Diameters check
    # main Diameter
    diameter = []
    for i in range(get_size()):
        diameter.append(game_list[i][i])
    if diameter[0] != " " and all(x == diameter[0] for x in diameter):
        if column[0] == 'X':
            return 0
        else:
            return 1

    # second diameter
    diameter = []
    for i in range(get_size()):
        diameter.append(game_list[i][get_size()-(i+1)])
    if diameter[0] != " " and all(x == diameter[0] for x in diameter):
        if column[0] == 'X':
            return 0
        else:
            return 1

    # draw check
    draw_check = True
    for row in game_list:
        for column in row:
            if column == ' ':
                draw_check = False
    if draw_check:
        return 2


def print_winner(index, names_list):
    if index == 2:
        print("DRAW!!")
    else:
        print(f"{names_list[index]} WINS!!")


_clear()
names = welcome()
table_size = get_size()
game_list = game_list_render(table_size)
winner = None

turn = 0
while(turn < table_size**2):
    _clear()
    print(names[0], names[1], sep=" vs ")
    table_render(game_list)
    turn = move(turn, names[int(turn % 2)], game_list)
    _clear()
    table_render(game_list)
    winner = win_check(game_list)
    if winner != None:
        break
    turn += 1

_clear()
table_render(game_list)
print_winner(winner, names)
sleep(5)
