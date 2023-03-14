from tkinter import *
from functools import partial


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
        pass


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    Menu()
    root.mainloop()
