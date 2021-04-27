from abc import ABC, abstractmethod
from Game import Game, GameError
from tkinter import Button, Tk, Frame, X, Toplevel, StringVar, Text, Scrollbar, Y, LEFT, RIGHT, END, Grid, N, S, W, E, Message
from itertools import product


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
        # note no double brackets after callback command, spaces to make it look nice
        Button(
            frame,
            text = 'Play',
            command = self._play_callback).pack(fill=X)
        
        Button(
            frame,
            text = 'Quit',
            command = self._quit_callback).pack(fill=X)
        
        console = Text(frame, heigh=4, width=50)
        scroll = Scrollbar(frame)
        scroll.pack(side=RIGHT, fill=Y)
        console.pack(side=LEFT, fill=Y)
        
        scroll.config(command=console.yview)
        console.config(yscrollcommand=scroll.set)
        
        self.__root = root
        self.__console = console
        self.__game_in_progress = False
        self.__help_open = False
        
    def _help_callback(self):
        if self.__help_open:
            return
        self.__help_open = True
        help_win = Toplevel(self.__root)  
        help_text = """Welcome To Tic Tac Toe!
The rules are:
    - Each player takes turns in placing their respective marker on the grid.
    - When a player lines up three of their markers vertically, horizontally, or diagonally, they win the game.
    - If no player is able to get 3 in a row, the game is drawn.

Good Luck! May the Tic Tac Toe gods smile upon you..."""
        
        self.__help_win = help_win
        Message(help_win, text=help_text).pack(fill=X)
        
        Button(help_win,
              text="Dismiss",
              command=self._dismiss_help).pack(fill=X)
        
    def _dismiss_help(self):
        self.__help_open = False
        self.__help_win.destroy()
    
    def _dismiss_game(self):
        self.__game_in_progress = False
        self.__game_win.destroy()

    def _play_callback(self):
        if self.__game_in_progress:
            return
        self.__game_in_progress = True
        self.__finished = False
        self.__game = Game()
        #game win as in game window
        game_win = Toplevel(self.__root)
        game_win.title("Game")
        frame = Frame(game_win)
        self.__game_win = game_win
        
        #Resizing
        Grid.columnconfigure(game_win, 0, weight=1)
        Grid.rowconfigure(game_win,0,weight=1)
        frame.grid(row=0,column=0, sticky=N+S+W+E)
        
        Button(game_win, text='Dismiss', command=self._dismiss_game).grid(row=1,column=0,sticky=N+S+W+E)
        
        #note this means only one window at a time, any other one's control will be whack
        self.__buttons = [[None] *3 for _ in range(3)]
        for row, col in product(range(3), range(3)):
            b = StringVar()
            b.set(self.__game.at(row+1,col+1))
            
            cmd = lambda r=row, c=col: self.__play_and_refresh(r,c)
            
            Button(frame, textvariable=b,command=cmd).grid(row=row,column=col, sticky=N+S+W+E)
            self.__buttons[row][col] = b
        
        #more resizing, epic.
        for i in range(3):
            Grid.columnconfigure(frame, i, weight=1)
            Grid.rowconfigure(frame,i,weight=1)
            
    def __play_and_refresh(self, row, col):
        if self.__finished:
            return
        
        try:
            self.__game.play(row+1,col+1)
        except GameError as e:
            self.__console.insert(END, f"{e}\n")
        
        #refresh
        for row, col in product(range(3), range(3)):
            text = self.__game.at(row+1,col+1)
            self.__buttons[row][col].set(text)
    
        w = self.__game.winner
        if w is not None:
            self.__finished = True
            if w is Game._DRAW:
                self.__console.insert(END, "The game has been drawn!\n")
            else:
                self.__console.insert(END, f"{w} has won, Congratulations!\n")
    
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