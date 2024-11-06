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
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame

    board.render()

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    py.display.flip()

    clock.tick(60)  # limits FPS to 60

py.quit()
