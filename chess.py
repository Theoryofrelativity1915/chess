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

example_pawn = Pawn(0, 0, WHITE)

while running:
    # poll for events
    # py.QUIT event means the user clicked X to close your window
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    board.render()
    example_pawn.render()

    # flip() the display to put your work on screen
    py.display.flip()

    clock.tick(60)  # limits FPS to 60

py.quit()
