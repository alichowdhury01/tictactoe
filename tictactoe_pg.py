import pygame, sys
import numpy as np


pygame.init()

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROW = 3
BOARD_COL = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55


# Color
BG_COLOR = (28, 170, 156)
RED = (255, 0, 0)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

# Board
board = np.zeros((BOARD_ROW, BOARD_COL))


def draw_lines():

    # Horizontal 1
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)

    # Horizontal 2
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

    # Vertical 1
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)

    # Vertical 2
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def draw_symbol():
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)


def player_moves(row, col, player):
    board[row][col] = player

def empty_cell(row, col):
    return board[row][col] == 0

def is_board_full():
    for row in range(BOARD_ROW):
        for col in range(BOARD_COL):
            if board[row][col] == 0:
                return False
    return True

draw_lines()

player = 1

# mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if empty_cell(clicked_row, clicked_col):
                if player == 1:
                    player_moves(clicked_row, clicked_col, 1)
                    player = 2

                elif player == 2:
                    player_moves(clicked_row, clicked_col, 2)
                    player = 1

                draw_symbol()

    pygame.display.update()