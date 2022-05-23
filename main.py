# import pygame
import numpy as np

ROWS = 6
COLUMNS = 7

column_free_location = np.array((5, 5, 5, 5, 5, 5, 5))
d = np.array(((1,2,3,4),(6,7,8)))
player1 = 1
player2 = 2

turnPlayer1 = True


def create_bord():
    bord = np.zeros((ROWS, COLUMNS))
    return bord


def print_bord(bord):
    print(bord)


def add_pieces(bord, color, column):
    if column_free_location[column] < 0:
        return False
    else:
        bord[column_free_location[column]][column] = color
        column_free_location[column] -= 1
    return True

def check_if_win(bord,position):


bord = create_bord()
add_pieces(bord, player1, 0)
add_pieces(bord, player2, 0)

print_bord(bord)
