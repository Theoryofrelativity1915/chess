# Contains the main game loop
import pygame as py
from board import Board


# py setup
py.init()
board = Board()
clock = py.time.Clock()
running = True


while running:
    # poll for events
    # py.QUIT event means the user clicked X to close your window
    current_piece = None
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            x, y = py.mouse.get_pos()
            col = int(x / 100)
            row = int(y / 100)
            # print(board.board[row][col].name())
            # print(row, col)
            board.print_board()
            if current_piece != None:  # There is already a piece selected
                current_piece.move(row, col)
                current_piece = None
            else:  # No piece selected, selecting piece
                current_piece = board.get_piece(row, col)
                if current_piece != None:
                    print("Piece!")
                    current_piece.select()

    board.render()

    # flip() the display to put your work on screen
    py.display.flip()

    clock.tick(60)  # limits FPS to 60

py.quit()
