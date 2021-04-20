from abc import ABC, abstractmethod
from Game import Game, GameError

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        print("Running Gui")

class Terminal(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        while not self._game.winner:
            print(self._game)
            try:
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
            except ValueError:
                print("Non-numeric imput")
                continue
            #range check, maybe make for Game _DIM
            if 1 <= row <= Game._DIM and 1<= col <= Game._DIM:
                try:
                    self._game.play(row, col)
                except GameError:
                    print("Invalid Input\n")
                    continue
            else:
                print("Row and Column outside of accepted range")
        print(self._game)        
        w = self._game.winner
        if w == Game._DRAW:
            print("This game was drawn")
        else:
            print(f"The winner was {w}, Congratulations!")