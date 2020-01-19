# Noughts and crosses game wrote on Python designed with with a graphical
# user interface and implemented using the Tkinter library.
# Noughts and crosses is a game for two players, X and O,
# who take turns marking the spaces in a 3×3 grid. The player
# who succeeds in placing three of their marks in a horizontal,
# vertical, or diagonal row wins the game.

# Ilya Pyshkin

from tkinter import *
import random
import time
from functools import partial

PICS = ["Untitled.png", "Player 1.png", "Player 2.png"]


class NoughtsAndCrosses:

    def __init__(self):
        """
        Constructor of the class NoughtsAndCrosses
        """
        self.__window = Tk()
        self.__window.title("Noughts and crosses")

        self.__turn = 0
        self.__pics = []
        for picfile in PICS:
            pic = PhotoImage(file=picfile, name=picfile.split(".")[0])
            self.__pics.append(pic)

        self.top_frame = Frame(self.__window)
        self.top_frame.grid()
        self.bottom_frame = Frame(self.__window)
        self.bottom_frame.grid()

        self.nc_label = Label(self.top_frame, text="Player 1 your turn")
        self.nc_label.grid(row=0)

        self.button_rows = []
        self.draw_board = True
        # Creating buttons with noughts and crosses
        for i in range(3):
            button_columns = []
            for j in range(3):
                new_button = Button(self.bottom_frame, image=self.__pics[0], command=partial(self.pic_changer, i, j))
                new_button.grid(row=i, column=j)
                button_columns.append(new_button)
            self.button_rows.append(button_columns)

        menubar = Menu(self.__window)
        menubar.add_command(label="New game", command=self.initialize_game)
        menubar.add_command(label="Exit", command=self.__window.destroy)
        self.__window.config(menu=menubar)

    def initialize_game(self):
        """
        Function reset the label
        :return: None
        """
        self.__turn = 0
        self.draw_board = True
        for i in range(3):
            for j in range(3):
                self.button_rows[i][j].configure(image=self.__pics[0])
        self.nc_label.configure(text="Player 1 your turn")

    def pic_changer(self, i, j):
        """
        Function process user click to the specified button
        :param i: row
        :param j: column
        :return: flag indicates end of the game
        """
        if self.draw_board is False:
            return
        mark = None
        if self.__turn % 2 == 0:
            self.button_rows[i][j].configure(image=self.__pics[1])
            mark = self.__pics[1].name
            self.nc_label.configure(text="Player 2 your turn")
        else:
            self.button_rows[i][j].configure(image=self.__pics[2])
            mark = self.__pics[2].name
            self.nc_label.configure(text="Player 1 your turn")
        self.__turn += 1
        if self.winner(mark) is False:
            self.draw_board = False
            return self.draw_board
        if self.__turn >= 9 and self.draw_board is True:
            self.nc_label.configure(text="Draw!")

    def winner(self, mark):
        """
        Function check game winner
        :param mark: name of the picture/player
        :return: flag indicates end of the game
        """
        for i in range(3):
            if self.button_rows[i][0].cget("image") == self.button_rows[i][1].cget("image") \
                    == self.button_rows[i][2].cget("image") == mark:
                self.nc_label.configure(text="The game ended, the winner is " + mark)
                self.draw_board = False
                return self.draw_board
            if self.button_rows[0][i].cget("image") == self.button_rows[1][i].cget("image")\
                    == self.button_rows[2][i].cget("image") == mark:
                self.nc_label.configure(text="The game ended, the winner is " + mark)
                self.draw_board = False
                return self.draw_board
        if self.button_rows[0][0].cget("image") == self.button_rows[1][1].cget("image")\
                == self.button_rows[2][2].cget("image") == mark or \
                self.button_rows[2][0].cget("image") == self.button_rows[1][1].cget("image") \
                == self.button_rows[0][2].cget("image") == mark:
            self.nc_label.configure(text="The game ended, the winner is " + mark)
            self.draw_board = False
            return self.draw_board

    def start(self):
        """
        Function starts the UI
        :return: None
        """
        self.__window.mainloop()


def main():
    u1 = NoughtsAndCrosses()
    u1.start()


main()
