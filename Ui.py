from abc import ABC, abstractmethod
from Game import Game, GameError
from tkinter import Button, Tk, Frame, X

class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = Tk()
        root.title("Tic Tac Toe")
        frame = Frame(root)
        frame.pack()
        
        Button(
            frame,
            text = 'Show Help',
            command = self._help_callback).pack(fill=X)
        
        Button(
            frame,
            text = 'Play',
            command = self._play_callback).pack(fill=X)
        
        Button(
            frame,
            text = 'Quit',
            command = self._quit_callback).pack(fill=X)
        
        
        self.__root = root
        
    def _help_callback(self):
        pass

    def _play_callback(self):
        pass
    
    def _quit_callback(self):
        self.__root.quit()
    
    
    def run(self):
        print("Running Gui")
        self.__root.mainloop()

        

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