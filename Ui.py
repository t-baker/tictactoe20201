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
        self.__game = Game()
        pass

    def run(self):
        while not self.__game.winner:
            print(self.__game)
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            self.__game.play(row, col)
        print("grats")