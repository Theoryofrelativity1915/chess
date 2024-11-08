# Contains all of the classes of the different pieces
import pygame as py
import os
from constants import SQUARE_SIZE, WHITE
white_pawn_image = py.image.load(os.path.join('./assets', 'white_pawn.png'))
black_pawn_image = py.image.load(os.path.join('./assets', 'black_pawn.png'))


class Pawn:
    def __init__(self, canvas, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        # Pygame starts drawing from the top left, so each piece needs its own
        # offset to be in the center of the square.
        self.render_offset = 18
        self.pos = (row * SQUARE_SIZE + self.render_offset,
                    col * SQUARE_SIZE + self.render_offset * 2)
        if (self.color == WHITE):
            self.image = white_pawn_image
        else:
            self.image = black_pawn_image

    def move(self):
        pass

    def delete(self):
        pass

    def render(self):
        self.canvas.blit(self.image, self.pos)
