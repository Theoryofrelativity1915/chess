# Contains the main game loop
import pygame as py
from board import Board
from constants import BLACK, WHITE


# py setup
py.init()
board = Board()
clock = py.time.Clock()
running = True

def get_user_input():
    x, y = py.mouse.get_pos()
    col = int(x / 100)
    row = int(y / 100)
    return [row, col]


def wait_and_move_piece(current_piece):
    if board.turn % 2 == 0:
        while current_piece is not None:  # There is already a piece selected
            for event in py.event.get():
                if event.type == py.QUIT:
                    exit(1)
                elif event.type == py.MOUSEBUTTONDOWN:
                    if current_piece.color == WHITE:
                        [row, col] = get_user_input()
                        current_piece.move(row, col, board)
                        board.turn += 1
                        return None
                    else:
                        return None
    else:
        while current_piece is not None:  # There is already a piece selected
            for event in py.event.get():
                if event.type == py.QUIT:
                    exit(1)
                elif event.type == py.MOUSEBUTTONDOWN:
                    if current_piece.color == BLACK:
                        [row, col] = get_user_input()
                        current_piece.move(row, col, board)
                        board.turn += 1
                        return None
                    else:
                        return None



def restart():
    return Board()


while running:
    # poll for events
    # py.QUIT event means the user clicked X to close your window
    current_piece = None
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            if board.game_over:
                x, y = py.mouse.get_pos()
                if (200 <= x <= 380 and 400 <= y <= 480):
                    board = restart()
                elif (400 <= x <= 580 and 400 <= y <= 480):
                    running = False
            [row, col] = get_user_input()
            if 0 <= row <= 7 and 0 <= col <= 7:
                current_piece = board.get_piece(row, col)
            if current_piece is not None:
                current_piece = wait_and_move_piece(current_piece)
    board.render(py.mouse.get_pos())
    # flip() the display to put your work on screen
    py.display.flip()

    clock.tick(60)  # limits FPS to 60

py.quit()
