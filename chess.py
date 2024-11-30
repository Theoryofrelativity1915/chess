# Contains the main game loop
import pygame as py
from board import Board


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
    while current_piece is not None:  # There is already a piece selected
        for event in py.event.get():
            if event.type == py.QUIT:
                exit(1)
            elif event.type == py.MOUSEBUTTONDOWN:
                [row, col] = get_user_input()
                print(current_piece.col, current_piece.row)
                current_piece.move(row, col, board)
                print(current_piece.col, current_piece.row)
                return None


while running:
    # poll for events
    # py.QUIT event means the user clicked X to close your window
    current_piece = None
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            [row, col] = get_user_input()
            current_piece = board.get_piece(row, col)
            if current_piece is not None:
                print("Piece selected!")
                current_piece.select()
                board.print_board()
                current_piece = wait_and_move_piece(current_piece)
                board.print_board()
                board.render()
    board.render()
    # flip() the display to put your work on screen
    py.display.flip()

    clock.tick(60)  # limits FPS to 60

py.quit()
