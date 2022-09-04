class Game():

    def __init__(self):
        self.turn = 0
    
    def changeTurn(self):
        self.turn = not self.turn

    def getTurn(self):
        return self.turn