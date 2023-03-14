from tkinter import *
from functools import partial
import csv
import random


# user chooses 3, 5, 10 rounds
class Menu:

    def __init__(self):
        # common format for all buttons
        # Arial size 14 bold with white text
        button_font = ("Arial", "14")
        button_fg = "#FFFFFF"

        # Set up GUI Frame
        self.menu_frame = Frame(padx=10, pady=10)
        self.menu_frame.grid()

        self.menu_heading = Label(self.menu_frame,
                                  text="Colour Quest",
                                  font=("Arial", "18", "bold"))
        self.menu_heading.grid(row=0)

        instructions = "In each round you will be given six different " \
                       "colours to choose from. pick a colour and see if " \
                       "you can beat the computer's score! \n\n" \
                       "To begin, chose how many rounds you d like to play..."
        self.menu_instructions = Label(self.menu_frame,
                                       text=instructions,
                                       wraplength=430, width=60,
                                       justify="left",
                                       pady=10)
        self.menu_instructions.grid(row=1)

        self.button_frame = Frame(self.menu_frame)
        self.button_frame.grid(row=4)

        btn_colour_value = [
            ["#CC0000", 3], ["#009900", 5], ["#000099", 10]
        ]

        column_var = 0
        for item in btn_colour_value:
            self.button = Button(self.button_frame,
                                 text="{} Rounds".format(item[1]),
                                 font=button_font, width=12,
                                 bg=item[0],
                                 fg=button_fg,
                                 command=lambda: self.to_play(item[1]))
            self.button.grid(row=0, column=column_var,
                             pady=5, padx=5)
            column_var += 1

    def to_play(self, num_rounds):
        Play(num_rounds)

        # hide Menu
        root.withdraw()


class Play:

    def __init__(self, how_many):
        self.play_box = Toplevel()

        # if users press cross at tip, closes help and
        # 'refuses' help button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play))

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        rounds_heading = "Choose - Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.quest_frame,
                                    text=rounds_heading,
                                    font=("Arial", "16", "bold"))
        self.choose_heading.grid(row=0)

        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)

        self.start_over_button = Button(self.control_frame,
                                        text="Start Over",
                                        command=self.close_play)
        self.start_over_button.grid(row=0, column=2)

    def close_play(self):
        # reshow menu
        # game / allow new game to start
        root.deiconify()
        self.play_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    Menu()
    root.mainloop()
