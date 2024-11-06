# Contains the entire board class
import pygame as py

from constants import BOARD_HEIGHT, BOARD_WIDTH, ROWS, COLS, WHITE, BLACK, MINT, GREEN, SQUARE_SIZE


class Board:
    def __init__(self):
        self.rows = ROWS
        self.cols = COLS
        self.canvas = py.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))

    def render(self):
        self.canvas.fill(MINT)
        self.draw_squares()
        self.draw_board_outline()

    def draw_board_outline(self):
        py.draw.rect(self.canvas, BLACK,
                     (COLS * SQUARE_SIZE, 0, 2, ROWS * SQUARE_SIZE))
        py.draw.rect(self.canvas, BLACK,
                     (0, 0, SQUARE_SIZE * COLS, 2))
        py.draw.rect(self.canvas, BLACK,
                     (0, 0, 2, ROWS * SQUARE_SIZE))
        py.draw.rect(self.canvas, BLACK,
                     (0, (ROWS * SQUARE_SIZE) - 2, COLS * SQUARE_SIZE, 2))

    def draw_squares(self):
        for i in range(ROWS):
            for j in range(COLS):
                if (i + j) % 2 == 0:
                    continue
                py.draw.rect(self.canvas, GREEN, (i * SQUARE_SIZE,
                                                  j * SQUARE_SIZE, SQUARE_SIZE,
                                                  SQUARE_SIZE))
