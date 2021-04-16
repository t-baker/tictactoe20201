
class Game:

    EMPTY = " "
    P1 = "o"
    P2 = "x"
    
    def __init__(self):
        self.__board = [[Game.EMPTY] * 3 for _ in range(3)]
        self.__player = Game.P1

    def __repr__(self):
        return "cba rn"
    
    
    def play(self,row,col):
        self.__board[row][col] = self.__player
        self.__player = Game.P2 if self.__player == Game.P1 else Game.P1
    
    @property
    def winner(self):
        if self.__board[0][0] == Game.P1 and self.__board[0][1] == Game.P1 and self.__board[0][2] == Game.P1:
            return True
        else:
            return False

if __name__ == "__main__":
    pass
