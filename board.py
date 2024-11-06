# Contains the entire board class
import pygame as py

from constants import BOARD_HEIGHT, BOARD_WIDTH, ROWS, COLS, WHITE, BLACK, SQUARE_SIZE


class Board:
    def __init__(self):
        self.rows = ROWS
        self.cols = COLS
        self.canvas = py.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))

    def render(self):
        self.canvas.fill(WHITE)
        for i in range(ROWS):
            for j in range(COLS):
                if (i + j) % 2 == 0:
                    continue
                py.draw.rect(self.canvas, BLACK, (i * SQUARE_SIZE,
                                                  j * SQUARE_SIZE, SQUARE_SIZE,
                                                  SQUARE_SIZE))
