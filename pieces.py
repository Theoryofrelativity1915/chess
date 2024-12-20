# Contains all of the classes of the different pieces
import pygame as py
import os
from constants import SQUARE_SIZE, WHITE, BLUE, BLACK
import board

# Pawn
white_pawn_image = py.image.load(os.path.join('./assets', 'white_pawn.png'))
black_pawn_image = py.image.load(os.path.join('./assets', 'black_pawn.png'))

# Rook
white_rook_image = py.image.load(os.path.join('./assets', 'white_rook.png'))
black_rook_image = py.image.load(os.path.join('./assets', 'black_rook.png'))

# Knight
white_knight_image = py.image.load(
    os.path.join('./assets', 'white_knight.png'))
black_knight_image = py.image.load(
    os.path.join('./assets', 'black_knight.png'))

# Bishop
white_bishop_image = py.image.load(
    os.path.join('./assets', 'white_bishop.png'))
black_bishop_image = py.image.load(
    os.path.join('./assets', 'black_bishop.png'))

# Queen
white_queen_image = py.image.load(os.path.join('./assets', 'white_queen.png'))
black_queen_image = py.image.load(os.path.join('./assets', 'black_queen.png'))

# King
white_king_image = py.image.load(os.path.join('./assets', 'white_king.png'))
black_king_image = py.image.load(os.path.join('./assets', 'black_king.png'))


class Piece:
    def __init__(self, canvas, row, col, color, image):
        self.row = row
        self.col = col
        self.color = color
        self.canvas = canvas
        self.image = image
        self.render_offset = 18
        self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                    self.row * SQUARE_SIZE + self.render_offset * 2)
        self.check_positions = set()
        self.name = None


class Pawn(Piece):
    def __init__(self, canvas, row, col, color):
        if (color == WHITE):
            image = white_pawn_image
        else:
            image = black_pawn_image
        super().__init__(canvas, row, col, color, image)
        self.add_pawn_check_positions()

    def select(self):  # Highlights possible moves
        print("Pawn selected")
        py.draw.rect(self.canvas, BLUE, (self.row * SQUARE_SIZE,
                                         (self.col + 1) *
                                         SQUARE_SIZE, SQUARE_SIZE,
                                         SQUARE_SIZE))
        py.draw.rect(self.canvas, BLUE, (self.row * SQUARE_SIZE,
                                         (self.col + 2) *
                                         SQUARE_SIZE, SQUARE_SIZE,
                                         SQUARE_SIZE))

    def is_valid_row_for_pawn(self, row, col, opponent):
        if ((col == self.col
             and opponent is None
             and self.color == BLACK
             and self.row == 1
             and abs(row - self.row) <= 2)):
            return True
        elif ((col == self.col
               and opponent is None
               and self.color == WHITE
               and self.row == 6
               and abs(row - self.row) <= 2)):
            return True
        elif (col == self.col
              and opponent is None
              and abs(self.row - row) == 1):
            return True
        elif (abs(col - self.col) == 1
              and opponent is not None
              and abs(self.row - row) == 1):
            return True
        return False

    def move(self, row, col, bd):  # Moves piece to designated square if possible
        if (row > 7 or row < 0 or col > 7 or col < 0) or (self.row == row and self.col == col):
            return
        selected_row_valid = False
        selected_col_valid = False
        opponent = bd.get_piece(row, col)
        if opponent is not None and opponent.color == self.color:
            opponent = None  # Can't kill a teammate
        if self.is_valid_row_for_pawn(row, col, opponent):
            selected_row_valid = True
        if (col == self.col or abs(self.col - col) == 1 and opponent is not None):
            selected_col_valid = True
        # If both the row they want to go and the col they want to go is valid, then let them and kill whatever is there.
        if selected_col_valid and selected_row_valid:
            bd.remove_piece(row, col)
            bd.board[row][col] = self
            bd.board[self.row][self.col] = None
            self.row = row
            self.col = col
            self.add_pawn_check_positions()
            self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                        self.row * SQUARE_SIZE + self.render_offset * 2)
        if (self.row == 0 and self.color == WHITE or self.row == 7 and self.color == BLACK):
            new_piece = Queen(self.canvas, self.row, self.col, self.color)
            bd.board[row][col] = new_piece

    def add_pawn_check_positions(self):
        self.check_positions.clear()
        if self.color == WHITE:
            self.check_positions.add((self.row - 1, self.col + 1))
            self.check_positions.add((self.row - 1, self.col - 1))
        else:
            self.check_positions.add((self.row + 1, self.col + 1))
            self.check_positions.add((self.row + 1, self.col - 1))

    # Pygame starts drawing from the top left, so each piece needs its own
    # offset to be in the center of the square.
    def render(self):
        self.canvas.blit(self.image, self.pos)

    def delete(self):
        pass

    def name(self):
        print("Pawn")


class Rook(Piece):

    def __init__(self, canvas, row, col, color):
        if (color == WHITE):
            image = white_rook_image
        else:
            image = black_rook_image
        super().__init__(canvas, row, col, color, image)

    def is_valid_move_for_rook(self, row, col):
        if (self.row == row) ^ (self.col == col):
            return True
        return False
    
    def rook_movement(self, row, col, bd):
        moved = False
        distancer = row - self.row
        distancec = col - self.col
        x = 1
        if row != self.row and distancer < 0: #Going up
            while x <= abs(row - self.row):
                opponent = bd.get_piece((self.row - x), col)
                if opponent is not None and opponent.color is not self.color:
                    bd.board[opponent.row][opponent.col] = self
                    bd.board[self.row][self.col] = None
                    self.row = opponent.row
                    self.col = opponent.col
                    self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                                self.row * SQUARE_SIZE + self.render_offset * 2)
                    bd.remove_piece_to_side_of_board(opponent)
                    moved = True
                    break
                elif opponent is not None and opponent.color is self.color:
                    moved = True
                    break
                x += 1
            if moved == False:
                bd.board[row][col] = self
                bd.board[self.row][self.col] = None
                self.row = row
                self.col = col
                self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                            self.row * SQUARE_SIZE + self.render_offset * 2)
        elif row != self.row and distancer > 0: #Going down
            while x <= abs(row - self.row):
                opponent = bd.get_piece((self.row + x), col)
                if opponent is not None and opponent.color is not self.color:
                    bd.board[opponent.row][opponent.col] = self
                    bd.board[self.row][self.col] = None
                    self.row = opponent.row
                    self.col = opponent.col
                    self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                                self.row * SQUARE_SIZE + self.render_offset * 2)
                    bd.remove_piece_to_side_of_board(opponent)
                    moved = True
                    break
                elif opponent is not None and opponent.color is self.color:
                    moved = True
                    break
                x += 1
            if moved == False:
                bd.board[row][col] = self
                bd.board[self.row][self.col] = None
                self.row = row
                self.col = col
                self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                            self.row * SQUARE_SIZE + self.render_offset * 2)
        elif col != self.col and distancec < 0: #Going right
            while x <= abs(col - self.col):
                opponent = bd.get_piece(row, (self.col - x))
                if opponent is not None and opponent.color is not self.color:
                    bd.board[opponent.row][opponent.col] = self
                    bd.board[self.row][self.col] = None
                    self.row = opponent.row
                    self.col = opponent.col
                    self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                                self.row * SQUARE_SIZE + self.render_offset * 2)
                    bd.remove_piece_to_side_of_board(opponent)
                    moved = True
                    break
                elif opponent is not None and opponent.color is self.color:
                    moved = True
                    break
                x += 1
            if moved == False:
                bd.board[row][col] = self
                bd.board[self.row][self.col] = None
                self.row = row
                self.col = col
                self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                            self.row * SQUARE_SIZE + self.render_offset * 2)
        elif col != self.col and distancec > 0: #Going left
            while x <= abs(col - self.col):
                opponent = bd.get_piece(row, (self.col + x))
                if opponent is not None and opponent.color is not self.color:
                    bd.board[opponent.row][opponent.col] = self
                    bd.board[self.row][self.col] = None
                    self.row = opponent.row
                    self.col = opponent.col
                    self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                                self.row * SQUARE_SIZE + self.render_offset * 2)
                    bd.remove_piece_to_side_of_board(opponent)
                    moved = True
                    break
                elif opponent is not None and opponent.color is self.color:
                    moved = True
                    break
                x += 1
            if moved == False:
                bd.board[row][col] = self
                bd.board[self.row][self.col] = None
                self.row = row
                self.col = col
                self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                            self.row * SQUARE_SIZE + self.render_offset * 2)

    def move(self, row, col, bd):  # Moves piece to designated square if possible
        # print("Rook selected")
        opponent = None
        if self.is_valid_move_for_rook(row, col):
           # print("valid move for rook")
           self.rook_movement(row, col, bd)


    def delete(self):
        pass

    def render(self):
        self.canvas.blit(self.image, self.pos)
        
    def name(self):
        print("Rook")

class Knight(Piece):
    def __init__(self, canvas, row, col, color):
        if (color == WHITE):
            image = white_knight_image
        else:
            image = black_knight_image
        super().__init__(canvas, row, col, color, image)

    def is_valid_move_for_knight(self, row, col):
        row += 1
        col += 1
        if ((abs(row - (self.row + 1))) + (abs(col - (self.col + 1))) == 3 and (row != 0 and col != 0)):
            print("Valid move for knight")
            return True
        else:
            return False

    def move(self, row, col, bd):
        opponent = None
        if self.is_valid_move_for_knight(row, col):
            opponent = bd.get_piece(row, col)
            if opponent is not None:
                if opponent.color is not self.color:
                    bd.remove_piece(row, col)
                    bd.board[row][col] = self
                    bd.board[self.row][self.col] = None
                    self.row = row
                    self.col = col
                    self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                                self.row * SQUARE_SIZE + self.render_offset * 2)

            else:
                bd.board[row][col] = self
                # print(bd.board[row][col])
                bd.board[self.row][self.col] = None
                # print(bd.board[self.row][self.col])
                self.row = row
                self.col = col
                self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                            self.row * SQUARE_SIZE + self.render_offset * 2)
            self.add_knight_check_positions(bd)

    def add_knight_check_positions(self, board):
        self.check_positions.clear()
        self.check_positions.add((self.row - 2, self.col - 1))
        self.check_positions.add((self.row - 2, self.col + 1))
        self.check_positions.add((self.row + 2, self.col - 1))
        self.check_positions.add((self.row + 2, self.col + 1))
        self.check_positions.add((self.row - 1, self.col - 2))
        self.check_positions.add((self.row - 1, self.col + 2))
        self.check_positions.add((self.row + 1, self.col - 2))
        self.check_positions.add((self.row + 1, self.col + 2))


    def render(self):
        self.canvas.blit(self.image, self.pos)


class Bishop(Piece):
    def __init__(self, canvas, row, col, color):
        if (color == WHITE):
            image = white_bishop_image
        else:
            image = black_bishop_image
        super().__init__(canvas, row, col, color, image)
        self.moves = set()
        self.visited = set()

    def check_bounds(self, row, col):
        if (row < 0 or
            row > 7 or
            col < 0 or
                col > 7):
            return False
        else:
            return True

    def iterate_all_diagonal_directions(self, valid_positions, row, col, row_iterator, col_iterator, board):
        row += row_iterator
        col += col_iterator
        while self.check_bounds(row, col):
            piece = board.get_piece(row, col)
            if piece is None:
                valid_positions.add((row, col))
                row += row_iterator
                col += col_iterator
            elif piece.color == self.color:
                return
            else:
                valid_positions.add((row, col))
                return

    def get_moves(self, board, positions):
        row, col = self.row, self.col
        self.iterate_all_diagonal_directions(
            positions, row, col, -1, -1, board)  # up and left
        self.iterate_all_diagonal_directions(
            positions, row, col, -1, +1, board)  # up and right
        self.iterate_all_diagonal_directions(
            positions, row, col, +1, +1, board)  # down and right
        self.iterate_all_diagonal_directions(
            positions, row, col, +1, -1, board)  # down and left

    def move(self, row, col, board):  # Moves piece to designated square if possible
        if (self.row == row and self.col == col):
            return
        self.visited.clear()
        self.moves.clear()
        self.get_moves(board, self.moves)
        if (row, col) in self.moves:
            board.remove_piece(row, col)
            board.board[row][col] = self
            board.board[self.row][self.col] = None
            self.row = row
            self.col = col
            self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                        self.row * SQUARE_SIZE + self.render_offset * 2)
            self.check_positions.clear()
            self.add_bishop_check_positions(board)

    def add_bishop_check_positions(self, board):
        self.get_moves(board, self.check_positions)

    def render(self):
        self.canvas.blit(self.image, self.pos)

    def name(self):
        print("Bishop")

    def __str__(self):
        return "Bishop"


class Queen(Piece):
    def __init__(self, canvas, row, col, color):
        if (color == WHITE):
            image = white_queen_image
        else:
            image = black_queen_image
        super().__init__(canvas, row, col, color, image)

class Queen(Piece):
    def __init__(self, canvas, row, col, color):
        if (color == WHITE):
            image = white_queen_image
        else:
            image = black_queen_image
        super().__init__(canvas, row, col, color, image)
        self.moves = set()
        self.visited = set()
        
    def using_rook(self, row, col):
        if (self.row == row) ^ (self.col == col):
            return True
        return False
    
    def check_bounds(self, row, col):
        if (row < 0 or
            row > 7 or
            col < 0 or
                col > 7):
            return False
        else:
            return True

    def iterate_all_diagonal_directions(self, valid_positions, row, col, row_iterator, col_iterator, board):
        row += row_iterator
        col += col_iterator
        while self.check_bounds(row, col):
            piece = board.get_piece(row, col)
            if piece is None:
                valid_positions.add((row, col))
                row += row_iterator
                col += col_iterator
            elif piece.color == self.color:
                return
            else:
                valid_positions.add((row, col))
                return

    def get_moves(self, board, positions):
        row, col = self.row, self.col
        self.iterate_all_diagonal_directions(
            positions, row, col, -1, -1, board)  # up and left
        self.iterate_all_diagonal_directions(
            positions, row, col, -1, +1, board)  # up and right
        self.iterate_all_diagonal_directions(
            positions, row, col, +1, +1, board)  # down and right
        self.iterate_all_diagonal_directions(
            positions, row, col, +1, -1, board)  # down and left

    def move(self, row, col, bd):
        if self.using_rook(row, col):
            Rook.rook_movement(self, row, col, bd)
        elif self.col != col and self.row != row:
            self.visited.clear()
            self.moves.clear()
            self.get_moves(bd, self.moves)
            if (row, col) in self.moves:
                bd.remove_piece(row, col)
                bd.board[row][col] = self
                bd.board[self.row][self.col] = None
                self.row = row
                self.col = col
                self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                            self.row * SQUARE_SIZE + self.render_offset * 2)
                self.check_positions.clear()
                self.add_queen_check_positions(bd)

    def add_queen_check_positions(self, board):
        self.get_moves(board, self.check_positions)

    def render(self):
        self.canvas.blit(self.image, self.pos)

    def name(self):
        print("Queen")


class King(Piece):
    def __init__(self, canvas, row, col, color):
        if (color == WHITE):
            image = white_king_image
        else:
            image = black_king_image
        super().__init__(canvas, row, col, color, image)
        self.name = "King"

    def is_adjacent_to_other_king(self, row, col, bd):
        for r in range(-1, 2):
            for c in range(-1, 2):
                if r == 0 and c == 0:
                    continue
                adjacent_row = row + r
                adjacent_col = col + c
                if 0 <= adjacent_row <= 7 and 0 <= adjacent_col <= 7:
                    piece = bd.get_piece(adjacent_row, adjacent_col)
                    if piece is not None and piece.color != self.color and isinstance(piece, King):
                        return True
        return False

    def select(self):
        py.draw.rect(self.canvas, BLUE, (self.row * SQUARE_SIZE,
                                         (self.col + 1) *
                                         SQUARE_SIZE, SQUARE_SIZE,
                                         SQUARE_SIZE))
        py.draw.rect(self.canvas, BLUE, (self.row * SQUARE_SIZE,
                                         (self.col + 2) *
                                         SQUARE_SIZE, SQUARE_SIZE,
                                         SQUARE_SIZE))

    def move(self, row, col, bd):
        if (row > 7 or row < 0 or col > 7 or col < 0) or (self.row == row and self.col == col):
            return
        if (bd.invalid_king_move(row, col, self.color)):
            return
        opponent = bd.get_piece(row, col)

        if opponent is not None and opponent.color == self.color:
            print("Occupied by a teammate")
            return

        if abs(self.row - row) <= 1 and abs(self.col - col) <= 1:
            if self.is_adjacent_to_other_king(row, col, bd):
                print("Invalid move: Kings must remain at least one space apart.")
                return
            bd.board[row][col] = self
            bd.board[self.row][self.col] = None
            self.row = row
            self.col = col
            self.pos = (self.col * SQUARE_SIZE + self.render_offset,
                        self.row * SQUARE_SIZE + self.render_offset * 2)
        else:
            print("Invalid move for the King.")

    def delete(self):
        pass

    def render(self):
        self.canvas.blit(self.image, self.pos)

    def name(self):
        print("King")

    def name(self):
        print("King")
