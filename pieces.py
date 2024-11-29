# Contains all of the classes of the different pieces
import pygame as py
import os
from constants import SQUARE_SIZE, WHITE
from board import Board

# Pawn
white_pawn_image = py.image.load(os.path.join('./assets', 'white_pawn.png'))
black_pawn_image = py.image.load(os.path.join('./assets', 'black_pawn.png'))

# Rook
white_rook_image = py.image.load(os.path.join('./assets', 'white_rook.png'))
black_rook_image = py.image.load(os.path.join('./assets', 'black_rook.png'))

# Knight
white_knight_image = py.image.load(os.path.join('./assets', 'white_knight.png'))
black_knight_image = py.image.load(os.path.join('./assets', 'black_knight.png'))

# Bishop
white_bishop_image = py.image.load(os.path.join('./assets', 'white_bishop.png'))
black_bishop_image = py.image.load(os.path.join('./assets', 'black_bishop.png'))

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
        self.pos = (col * SQUARE_SIZE + self.render_offset,
                    row * SQUARE_SIZE + self.render_offset * 2)

class Pawn(Piece):
    def __init__(self, canvas, row, col, color):
        if (color == WHITE):
            image = white_pawn_image
        else:
            image = black_pawn_image
        super().__init__(canvas, row, col, color, image)
    
    def select(self): #Highlights possible moves
        py.draw.rect(self.canvas, BLUE, (self.row * SQUARE_SIZE,
                                          (self.col + 1) * SQUARE_SIZE, SQUARE_SIZE,
                                          SQUARE_SIZE))
        py.draw.rect(self.canvas, BLUE, (self.row * SQUARE_SIZE,
                                          (self.col + 2) * SQUARE_SIZE, SQUARE_SIZE,
                                          SQUARE_SIZE))

    def move(self, row, col): #Moves piece to designated square if possible
        if self.row == 7 or 1: #Checks if pawn is in starting position
            if row == self.row + 1 or self.row + 2:
                opponent = Board.get_piece(row, col)
                if opponent != None:
                    opponent.delete()
                self.row = row
                self.col = col
        else:
            if row == self.row + 1:
                opponent = Board.get_piece(row, col)
                if opponent != None:
                    opponent.delete()
                self.row = row
                self.col = col

    def delete(self):
        pass

    # Pygame starts drawing from the top left, so each piece needs its own
    # offset to be in the center of the square.
    def render(self):
        self.canvas.blit(self.image, self.pos)

class Rook(Piece):
    self.moves[40]; #List to save current possible moves
    def __init__(self, canvas, row, col, color):
        if (color == WHITE):
            image = white_rook_image
        else:
            image = black_rook_image
        super().__init__(canvas, row, col, color, image)

    def select(self): #Highlights possible moves
        row = self.row
        col = self.col
        i = 0
        self.moves.clear()
        while row < 7:
            self.moves[i] = py.draw.rect(self.canvas, BLUE, ((row + 1) * SQUARE_SIZE,
                                             col * SQUARE_SIZE, SQUARE_SIZE,
                                             SQUARE_SIZE))
            row += 1
            i += 1
        while col < 7:
            self.moves[i] = py.draw.rect(self.canvas, BLUE, (row * SQUARE_SIZE,
                                             (col + 1) * SQUARE_SIZE, SQUARE_SIZE,
                                             SQUARE_SIZE))
            col += 1
            i += 1
        row = self.row
        col = self.col
        while row > -1:
            self.moves[i] = py.draw.rect(self.canvas, BLUE, ((row - 1) * SQUARE_SIZE,
                                             col * SQUARE_SIZE, SQUARE_SIZE,
                                             SQUARE_SIZE))
            row -= 1
            i += 1
        while col > -1:
            self.moves[i] = py.draw.rect(self.canvas, BLUE, (row * SQUARE_SIZE,
                                             (col - 1) * SQUARE_SIZE, SQUARE_SIZE,
                                             SQUARE_SIZE))
            col -= 1
            i += 1
        
    def move(self, row, col): #Moves piece to designated square if possible
        for x in self.moves:
            if self.moves[x].collidepoint(row, col):
                opponent = Board.get_piece(row, col)
                if opponent != None:
                    opponent.delete()
                self.row = row
                self.col = col
                break

    def delete(self):
        pass

    def render(self):
        self.canvas.blit(self.image, self.pos)

class Knight(Piece):
    def __init__(self, canvas, row, col, color):
        if (color == WHITE):
            image = white_knight_image
        else:
            image = black_knight_image
        super().__init__(canvas, row, col, color, image)

    def move(self):
        pass

    def delete(self):
        pass

    def render(self):
        self.canvas.blit(self.image, self.pos)

class Bishop(Piece):
    def __init__(self, canvas, row, col, color):
        if (color == WHITE):
            image = white_bishop_image
        else:
            image = black_bishop_image
        super().__init__(canvas, row, col, color, image)

    def select(self): #Highlights possible moves
        i = 0;
        self.moves.clear()
        row = self.row
        col = self.col
        while row and col < 7:
            self.moves[i] = py.draw.rect(self.canvas, BLUE, ((row + 1) * SQUARE_SIZE,
                                             (col + 1) * SQUARE_SIZE, SQUARE_SIZE,
                                             SQUARE_SIZE))
            row += 1
            row += 1
            i += 1
        while row > -1 and col < 7:
            self.moves[i] = py.draw.rect(self.canvas, BLUE, ((row - 1) * SQUARE_SIZE,
                                             (col + 1) * SQUARE_SIZE, SQUARE_SIZE,
                                             SQUARE_SIZE))
            row -= 1
            col += 1
            i += 1
        row = self.row
        col = self.col
        while row < 7 and col > -1:
            self.moves[i] = py.draw.rect(self.canvas, BLUE, ((row + 1) * SQUARE_SIZE,
                                             (col - 1) * SQUARE_SIZE, SQUARE_SIZE,
                                             SQUARE_SIZE))
            row += 1
            col -= 1
            i += 1
        while row and col > -1:
            py.draw.rect(self.canvas, BLUE, ((row - 1)* SQUARE_SIZE,
                                             (col - 1) * SQUARE_SIZE, SQUARE_SIZE,
                                             SQUARE_SIZE))
            row -= 1
            col -= 1
            i += 1
            
    def move(self, row, col): #Moves piece to designated square if possible
        for x in self.moves:
            if self.moves[x].collidepoint(row, col):
                opponent = Board.get_piece(row, col)
                if opponent != None:
                    opponent.delete()
                self.row = row
                self.col = col
                break

    def delete(self):
        pass

    def render(self):
        self.canvas.blit(self.image, self.pos)

class Queen(Piece):
    def __init__(self, canvas, row, col, color):
        if (color == WHITE):
            image = white_queen_image
        else:
            image = black_queen_image
        super().__init__(canvas, row, col, color, image)

    def move(self):
        pass

    def delete(self):
        pass

    def render(self):
        self.canvas.blit(self.image, self.pos)

class King(Piece):
    def __init__(self, canvas, row, col, color):
        if (color == WHITE):
            image = white_king_image
        else:
            image = black_king_image
        super().__init__(canvas, row, col, color, image)

    def move(self):
        pass

    def delete(self):
        pass

    def render(self):
        self.canvas.blit(self.image, self.pos)
