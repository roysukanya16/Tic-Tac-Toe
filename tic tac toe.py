import pygame, sys
import numpy as np

pygame.init()

WIDTH = 600
HEIGHT = 600
L_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCE_RADIUS = 60
CIRCLE_WIDTH = 15
space = 40
# colors
BG_COLOR = (28, 170, 156)
L_COLOR = (23, 145, 135)
C_COLOR = (245, 238, 215)
X_COLOR = (56, 56, 54)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)

# board
board = np.zeros((BOARD_ROWS, BOARD_COLS))


def draw_lines():
    # horizontal
    pygame.draw.line(screen, L_COLOR, (0, 200,), (600, 200), L_WIDTH)
    pygame.draw.line(screen, L_COLOR, (0, 400,), (600, 400), L_WIDTH)
    # vertical
    pygame.draw.line(screen, L_COLOR, (200, 0,), (200, 600), L_WIDTH)
    pygame.draw.line(screen, L_COLOR, (400, 0,), (400, 600), L_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, C_COLOR, ((int(col * 200 + 200 / 2)), (int(row * 200 + 200 / 2))),
                                   CIRCE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, X_COLOR, (col * 200 + space, row * 200 + 200 - space),
                                 (col * 200 + 200 - space, row * 200 + space), L_WIDTH)
                pygame.draw.line(screen, X_COLOR, (col * 200 + space, row * 200 + space),
                                 (col * 200 + 200 - space, row * 200 + 200 - space), L_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def avail_square(row, col):
    return board[row][col] == 0
    # SAME AS
    # if board[row][col] == 0:
    # return True
    # else:
    #  return False


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


def check_win(player):
    # vertical win chweck
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_ver_win_line(col, player)
            return True
    # horizontal win line
    for row in range(BOARD_COLS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_hori_win_line(row, player)
            return True
    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    # des diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_des_diagonal(player)
        return True

    return False


def draw_ver_win_line(col, player):
    posx = col * 200 + 100
    if player == 1:
        color = C_COLOR
    elif player == 2:
        color = X_COLOR
    pygame.draw.line(screen, color, (posx, 15), (posx, HEIGHT - 15), L_WIDTH)


def draw_hori_win_line(row, player):
    posy = row * 200 + 100
    if player == 1:
        color = C_COLOR
    elif player == 2:
        color = X_COLOR
    pygame.draw.line(screen, color, (15, posy), (WIDTH - 15, posy), L_WIDTH)


def draw_asc_diagonal(player):
    if player == 1:
        color = C_COLOR
    if player == 2:
        color = X_COLOR
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), L_WIDTH)


def draw_des_diagonal(player):
    if player == 1:
        color = C_COLOR
    if player == 2:
        color = X_COLOR
    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), L_WIDTH)


def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


draw_lines()
player = 1
game_over = False
# mainloop
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex = event.pos[0]  # retiurns the x coordinate of mouse
            mousey = event.pos[1]  # returns the y coordinate of mouse

            clicked_row = int(mousey // 200)
            clicked_col = int(mousex // 200)  # print(clicked_row)# print(clicked_col)
            if avail_square(clicked_row, clicked_col) and not game_over:
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                draw_figures()
        if event.type == pygame.KEYDOWN:
            if pygame.key == pygame.K_SPACE:
                restart()

    pygame.display.update()
