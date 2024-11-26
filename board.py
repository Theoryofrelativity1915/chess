# Contains the entire board class
import pygame as py
from pieces import Pawn
from constants import BOARD_HEIGHT, BOARD_WIDTH, ROWS, COLS, WHITE, BLACK, MINT, GREEN, SQUARE_SIZE


class Board:
    def __init__(self):
        self.rows = ROWS
        self.cols = COLS
        self.canvas = py.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
        # self.board = self.init_board_and_pieces()
        self.board = self.init_board_and_pieces()
        self.render_pieces()

    def render(self):
        self.canvas.fill(MINT)
        self.draw_squares()
        self.draw_board_outline()
        self.render_pieces()

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

    def init_board_and_pieces(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                match i:
                    case 0:
                        # render black pieces
                        new_piece = self.determine_piece_by_col(i, j)
                    case 1:
                        new_piece = Pawn(self.canvas, i, j, BLACK)
                    case 6:
                        new_piece = Pawn(self.canvas, i, j, WHITE)
                    case 7:
                        new_piece = self.determine_piece_by_col(i, j)
                board[i][j] = new_piece
        return board

    # Given a row and column, return the correct piece.
    def determine_piece_by_col(self, i, j):
        if i == 0:
            color = BLACK
        else:
            color = WHITE
        # Select correct black piece
        if j == 0 or j == 7:
            # return Rook(self.canvas, i, j, color)
            pass
        elif j == 1 or j == 6:
            # return Knight(self.canvas, i, j, color)
            pass
        elif j == 2 or j == 5:
            # return Bishop(self.canvas, i, j, color)
            pass
        elif j == 3:
            # return Queen(self.canvas, i, j, color)
            pass
        else:
            # return King(self.canvas, i, j, color)
            pass

    def render_pieces(self):
        for i in range(8):
            for j in range(8):
                # TODO: Remove this later when all of the pieces are actually being returned.
                if i == 1 or i == 6:
                    self.board[i][j].render()

    def get_piece(self, row, col):
        if (row > 7 or col > 7):
            raise Exception(
                "Uh-oh! Looks like the row or column was greater than 7. Please ensure that the row and column are less than 8.")
        return self.board[row][col]
