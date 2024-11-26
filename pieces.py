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
        self.canvas = canvas
        # Pygame starts drawing from the top left, so each piece needs its own
        # offset to be in the center of the square.
        self.render_offset = 18
        self.pos = (col * SQUARE_SIZE + self.render_offset,
                    row * SQUARE_SIZE + self.render_offset * 2)
        if (self.color == WHITE):
            self.image = white_pawn_image
        else:
            self.image = black_pawn_image

    def select(self): #Highlights possible moves
        py.draw.rect(self.canvas, BLUE, self.col + 1)
        py.draw.rect(self.canvas, BLUE, self.col + 2)

    def move(self, row, col): #Moves pawn to designated square if possible
        if self.row == 7:
            if row == self.row + 1 or row == self.row + 2:
                self.row = row
                self.col = col
        else:
            if row == self.row:
                self.row = row
                self.col = col

    def delete(self):
        pass

    def render(self):
        self.canvas.blit(self.image, self.pos)
