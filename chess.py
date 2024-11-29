# Contains the main game loop
import pygame as py
from board import Board
from constants import WHITE
from pieces import Pawn


# py setup
py.init()
board = Board()
clock = py.time.Clock()
running = True


while running:
    # poll for events
    # py.QUIT event means the user clicked X to close your window
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            x, y = py.mouse.get_pos()
            col = int(x/ 100)
            row = int(y / 100)
            print(row, col)
            if currentPiece != None: #There is already a piece selected
                currentPiece.move(row, col)
                currentPiece = None
            else: #No piece selected, selecting piece
                currentPiece = board.get_piece(row, col)
                if currentPiece != None:
                    print("Piece!")
                    currentPiece.select()

    board.render()

    # flip() the display to put your work on screen
    py.display.flip()

    clock.tick(60)  # limits FPS to 60

py.quit()
