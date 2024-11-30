# Contains the entire board class
import pygame as py
import pieces
from constants import BOARD_HEIGHT, BOARD_WIDTH, ROWS, COLS, WHITE, BLACK, MINT, GREEN, SQUARE_SIZE


class Board:
    def __init__(self):
        self.rows = ROWS
        self.cols = COLS
        self.canvas = py.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
        # self.board = self.init_board_and_pieces()
        self.board = self.init_board_and_pieces()
        self.render_pieces()
        self.removed_white_pieces = [
            [None for j in range(4)] for i in range(4)]
        self.removed_black_pieces = [
            [None for j in range(4)] for i in range(4)]
        # for i in range(len(self.removed_black_pieces)):
        #     for j in range(len(self.removed_black_pieces[0])):
        #         self.removed_white_pieces[i][j] = pieces.Pawn(
        #             self.canvas, 0, 0, WHITE)
        #         self.removed_black_pieces[i][j] = pieces.Pawn( self.canvas, 0, 0, BLACK)
        # self.remove_piece_to_side_of_board(piece=piece)

    def render(self):
        self.canvas.fill(MINT)
        self.draw_squares()
        self.draw_board_outline()
        self.render_pieces()
        self.render_removed_pieces()

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

    def invalid_king_move(self, row, col, color_of_king):
        for r in range(8):
            for c in range(8):
                piece = self.get_piece(r, c)
                if piece is not None:
                    if ((row, col) in piece.check_positions 
                        and piece.color != color_of_king):
                        return True
        return False

    def init_board_and_pieces(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        for row in range(8):
            for col in range(8):
                match row:
                    case 0:
                        # render black pieces
                        new_piece = self.init_piece_by_pos(row, col)
                    case 1:
                        new_piece = pieces.Pawn(self.canvas, row, col, BLACK)
                    case 6:
                        new_piece = pieces.Pawn(self.canvas, row, col, WHITE)
                    case 7:
                        new_piece = self.init_piece_by_pos(row, col)
                    case _:
                        new_piece = None
                board[row][col] = new_piece
        return board

    # Given a row and column, return the correct piece.
    def init_piece_by_pos(self, row, col):
        if row == 0:
            color = BLACK
        else:
            color = WHITE
        # Select correct black piece
        if col == 0 or col == 7:
            return pieces.Rook(self.canvas, row, col, color)
        elif col == 1 or col == 6:
            return pieces.Knight(self.canvas, row, col, color)
        elif col == 2 or col == 5:
            return pieces.Bishop(self.canvas, row, col, color)
        elif col == 3:
            return pieces.Queen(self.canvas, row, col, color)
        else:
            return pieces.King(self.canvas, row, col, color)

    def render_pieces(self):
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece is not None:
                    piece.render()

    def render_removed_pieces(self):
        white_row_offset = 400
        black_row_offset = 0
        self.render_removed_pieces_helper(
            self.removed_black_pieces, black_row_offset)
        self.render_removed_pieces_helper(
            self.removed_white_pieces, white_row_offset)

    def render_removed_pieces_helper(self, removed_pieces, row_offset, col_offset=800):
        for row in range(len(removed_pieces)):
            for col in range(len(removed_pieces[0])):
                # This case handles rendering a dead piece
                piece = removed_pieces[row][col]
                if piece is not None:
                    self.canvas.blit(
                        piece.image, ((col * 60 + col_offset),
                                      (row * 100) + row_offset))

    def get_piece(self, row, col):
        if (row > 7 or col > 7):
            raise Exception(
                "Uh-oh! Looks like the row or column was greater than 7. Please ensure that the row and column are less than 8.")
        return self.board[row][col]

    def remove_piece_to_side_of_board(self, piece):
        color = piece.color
        if color == WHITE:
            self.remove_piece_to_side_of_board(
                self.removed_white_pieces, piece)
        else:
            self.remove_piece_to_side_of_board(
                self.removed_black_pieces, piece)

    def remove_piece_to_side_of_board_helper(self, removed_pieces, piece):
        for row in range(len(removed_pieces)):
            for col in range(len(removed_pieces[0])):
                if removed_pieces[row][col] is not None:
                    removed_pieces[row][col] = piece

    def print_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                print(f'Row: {i}\tCol: {j}\tPiece: {self.board[i][j]}')
