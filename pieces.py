from abc import ABC

def isEmptySpace(x, y):
    i = y
    j = x
    return isinstance(board[i][j], EmptySpace)

class Piece(ABC):

    def __init__(self, p, x, y):
        self.player = p
        self.x = x
        self.y = y

    def isEnemyPiece(self, x, y):
        i = y
        j = x
        if self.player == 0:
            return board[i][j].getPlayer() == 1
        elif self.player == 1:
            return board[i][j].getPlayer() == 0
        else:
            return False

    def isFriendlyPiece(self, x, y):
        i = y
        j = x
        if self.player == 0:
            return board[i][j].getPlayer() == 0
        elif self.player == 1:
            return board[i][j].getPlayer() == 1
        else:
            return False

    def moveTo(self, x, y):
        board[self.y][self.x] = EmptySpace(self.x, self.y)
        board[y][x] = self

        self.x = x
        self.y = y

        return 1

    def move(self, destX, destY):
        pass

    def getPlayer(self):
        return self.player

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setPlayer(self, p):
        self.player = p

    def setPosition(self, x, y):
        self.x = x
        self.y = y

class Pawn(Piece):

    def __init__(self, p, x, y):
        super().__init__(p, x, y)
        self.startingX = x
        self.startingY = y

    def moveTo(self, x, y):
        board[self.y][self.x] = EmptySpace(self.x, self.y)
        if self.player == 0 and y == 7 or self.player == 1 and y == 0:
            board[y][x] = Queen(self.player, x, y)
        else:
            board[y][x] = self

        self.x = x
        self.y = y

        return 1

    def move(self, destX, destY):
        match self.player:
            case 0:

                if destX == self.x and destY == self.y + 1 and isEmptySpace(self.x, self.y + 1):
                    return self.moveTo(destX, destY)
                elif destX == self.x and destY == self.y + 2 and isEmptySpace(self.x, self.y + 2) and self.x == self.startingX and self.y == self.startingY:
                    return self.moveTo(destX, destY)
                elif destX == self.x - 1 and destY == self.y + 1 and self.isEnemyPiece(destX, destY):
                    return self.moveTo(destX, destY)
                elif destX == self.x + 1 and destY == self.y + 1 and self.isEnemyPiece(destX, destY):
                    return self.moveTo(destX, destY)
                
                return 0
                
            case 1: 

                if destX == self.x and destY == self.y - 1 and isEmptySpace(self.x, self.y - 1):
                    return self.moveTo(destX, destY)
                elif destX == self.x and destY == self.y - 2 and isEmptySpace(self.x, self.y - 2) and self.x == self.startingX and self.y == self.startingY:
                    return self.moveTo(destX, destY)
                elif destX == self.x - 1 and destY == self.y - 1 and self.isEnemyPiece(destX, destY):
                    return self.moveTo(destX, destY)
                elif destX == self.x + 1 and destY == self.y - 1 and self.isEnemyPiece(destX, destY):
                    return self.moveTo(destX, destY)
                
                return 0

class Rook(Piece):

    def __init__(self, p, x, y):
        super().__init__(p, x, y)

    def move(self, destX, destY):
        if destX == self.x:
            if destX < self.x:
                for i in range(self.x - 1, destX, -1):
                    if not isEmptySpace(i, self.y):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)
            if destX > self.x:
                for i in range(self.x + 1, destX):
                    if not isEmptySpace(i, self.y):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)
        if destY == self.y:
            if destY < self.y:
                for i in range(self.y - 1, destY, -1):
                    if not isEmptySpace(self.x, i):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)
            if destY > self.y:
                for i in range(self.y + 1, destY):
                    if not isEmptySpace(self.x, i):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)

        return 0

class Knight(Piece):

    def __init__(self, p, x, y):
        super().__init__(p, x, y)

    def move(self, destX, destY):
        potentialMoves = [(self.x - 2, self.y - 1), (self.x - 1, self.y - 2), (self.x + 1, self.y - 2), (self.x + 2, self.y - 1), 
                          (self.x + 2, self.y + 1), (self.x + 1, self.y + 2), (self.x - 1, self.y + 2), (self.x - 2, self.y + 1)]

        if (destX, destY) in potentialMoves and not self.isFriendlyPiece(destX, destY):
            return self.moveTo(destX, destY)
        
        return 0

class Bishop(Piece):

    def __init__(self, p, x, y):
        super().__init__(p, x, y)

    def move(self, destX, destY):
        if destX - self.x == destY - self.y:
            if destX < self.x and destY < self.y:
                for i in range(1, self.x - destX):
                    if not isEmptySpace(self.x - i, self.y - i):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)
            elif destX > self.x and destY < self.y:
                for i in range(1, destX - self.x):
                    if not isEmptySpace(self.x + i, self.y - i):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)
            elif destX < self.x and destY > self.y:
                for i in range(1, self.x - destX):
                    if not isEmptySpace(self.x - i, self.y + i):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)
            elif destX > self.x and destY > self.y:
                for i in range(1, destX - self.x):
                    if not isEmptySpace(self.x + i, self.y + i):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)
        
        return 0

class King(Piece):

    def __init__(self, p, x, y):
        super().__init__(p, x, y)

    def move(self, destX, destY):
        if destX - self.x <= 1 and destY - self.y <= 1 and (destX - self.x > 0 or destY - self.y > 0) and not self.isFriendlyPiece(destX, destY):
            return self.moveTo(destX, destY)
        else:
            return 0

class Queen(Piece):

    def __init__(self, p, x, y):
        super().__init__(p, x, y)

    def move(self, destX, destY):
        if destX == self.x:
            if destX < self.x:
                for i in range(self.x - 1, destX, -1):
                    if not isEmptySpace(i, self.y):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)
            if destX > self.x:
                for i in range(self.x + 1, destX):
                    if not isEmptySpace(i, self.y):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)
        if destY == self.y:
            if destY < self.y:
                for i in range(self.y - 1, destY, -1):
                    if not isEmptySpace(self.x, i):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)
            if destY > self.y:
                for i in range(self.y + 1, destY):
                    if not isEmptySpace(self.x, i):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)

        if destX - self.x == destY - self.y:
            if destX < self.x and destY < self.y:
                for i in range(1, self.x - destX):
                    if not isEmptySpace(self.x - i, self.y - i):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)
            elif destX > self.x and destY < self.y:
                for i in range(1, destX - self.x):
                    if not isEmptySpace(self.x + i, self.y - i):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)
            elif destX < self.x and destY > self.y:
                for i in range(1, self.x - destX):
                    if not isEmptySpace(self.x - i, self.y + i):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)
            elif destX > self.x and destY > self.y:
                for i in range(1, destX - self.x):
                    if not isEmptySpace(self.x + i, self.y + i):
                        return 0
                if self.isFriendlyPiece(destX, destY):
                    return 0

                return self.moveTo(destX, destY)

        return 0

class EmptySpace(Piece):

    def __init__(self, x, y):
        self.player = -1
        self.x = x
        self.y = y

    def move(self, destX, destY):
        return 0
        
board = [[Rook(0, 0, 0), 
          Knight(0, 1, 0), 
          Bishop(0, 2, 0), 
          Queen(0, 3, 0), 
          King(0, 4, 0), 
          Bishop(0, 5, 0), 
          Knight(0, 6, 0),
          Rook(0, 7, 0)],
         [Pawn(0, 0, 1),
          Pawn(0, 1, 1),
          Pawn(0, 2, 1),
          Pawn(0, 3, 1),
          Pawn(0, 4, 1),
          Pawn(0, 5, 1),
          Pawn(0, 6, 1),
          Pawn(0, 7, 1)],
         [EmptySpace(0, 2),
          EmptySpace(1, 2),
          EmptySpace(2, 2),
          EmptySpace(3, 2),
          EmptySpace(4, 2),
          EmptySpace(5, 2),
          EmptySpace(6, 2),
          EmptySpace(7, 2)],
         [EmptySpace(0, 3),
          EmptySpace(1, 3),
          EmptySpace(2, 3),
          EmptySpace(3, 3),
          EmptySpace(4, 3),
          EmptySpace(5, 3),
          EmptySpace(6, 3),
          EmptySpace(7, 3)],
         [EmptySpace(0, 4),
          EmptySpace(1, 4),
          EmptySpace(2, 4),
          EmptySpace(3, 4),
          EmptySpace(4, 4),
          EmptySpace(5, 4),
          EmptySpace(6, 4),
          EmptySpace(7, 4)],
         [EmptySpace(0, 5),
          EmptySpace(1, 5),
          EmptySpace(2, 5),
          EmptySpace(3, 5),
          EmptySpace(4, 5),
          EmptySpace(5, 5),
          EmptySpace(6, 5),
          EmptySpace(7, 5)],
         [Pawn(1, 0, 6),
          Pawn(1, 1, 6),
          Pawn(1, 2, 6),
          Pawn(1, 3, 6),
          Pawn(1, 4, 6),
          Pawn(1, 5, 6),
          Pawn(1, 6, 6),
          Pawn(1, 7, 6)],
         [Rook(1, 0, 7), 
          Knight(1, 1, 7), 
          Bishop(1, 2, 7), 
          Queen(1, 3, 7), 
          King(1, 4, 7), 
          Bishop(1, 5, 7), 
          Knight(1, 6, 7),
          Rook(1, 7, 7)]]