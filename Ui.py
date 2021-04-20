from abc import ABC, abstractmethod
from Game import Game

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
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            self._game.play(row, col)
        
        print(self._game)
        w = self._game.winner
        print(f"The winner was {w}, Congratulations!")