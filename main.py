""" Tic Tac Toe
----------------------------------------
"""
import random
import sys

board = [i for i in range(0, 9)]
player, computer = '', ''
# Corners, Center and Others, respectively
moves = ((1, 7, 3, 10), (5,), (2, 4, 6, 8))
# Winner combinations
winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
# Table
tab = range(1, 10)


def print_board():
    x = 1
    for i in board:
        end = ' | '
        if x % 3 == 0:
            end = ' \n'
            if i != 1:
                end += '---------\n'
        char = ' '
        if i in ('X', 'O'):
            char = i
        x += 1
        print(char, end=end)


def select_char():
    chars = ('X', 'O')
    if random.randint(0, 1) == 0:
        return chars[::-1]
    return chars


def can_move(brd, argplayer, argmove):
    if argmove in tab and brd[argmove - 1] == argmove - 1:
        return True
    return False


def can_win(brd, argplayer, argmove):
    places = []
    x = 0
    for i in brd:
        if i == argplayer: places.append(x);
        x += 1
    win = True
    for tup in winners:
        win = True
        for ix in tup:
            if brd[ix] != argplayer:
                win = False
                break
        if win:
            break
    return win


def make_move(brd, argplayer, argmove, undo=False):
    if can_move(brd, argplayer, argmove):
        brd[argmove - 1] = argplayer
        win = can_win(brd, argplayer, argmove)
        if undo:
            brd[argmove - 1] = argmove - 1
        return True, win
    return False, False


# AI goes here
def computer_move():
    lmove = -1
    # If I can win, others do not matter.
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            lmove = i
            break
    if lmove == -1:
        # If player can win, block him.
        for i in range(1, 10):
            if make_move(board, player, i, True)[1]:
                lmove = i
                break
    if lmove == -1:
        # Otherwise, try to take one of desired places.
        for tup in moves:
            for mv in tup:
                if lmove == -1 and can_move(board, computer, mv):
                    lmove = mv
                    break
    return make_move(board, computer, lmove)


def space_exist():
    return board.count('X') + board.count('O') != 9


player, computer = select_char()
print('Player is [%s] and computer is [%s]' % (player, computer))
result = '%%% Deuce ! %%%'
while space_exist():
    print_board()
    print('#Make your move ! [1-9] : ', end='')
    move = int(input())
    moved, won = make_move(board, player, move)
    if not moved:
        print(' >> Invalid number ! Try again !')
        continue
    #
    if won: '*** Congrats ! You won ! ***'
        # TODO

        break
    elif computer_move()[1]:
        result = '=== You lose ! =='
        break
print_board()
print(result)
