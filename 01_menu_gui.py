from tkinter import *


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

        self.three_button = Button(self.button_frame,
                                   text="3 Rounds",
                                   font=button_font, width=12,
                                   bg="#CC0000",
                                   fg=button_fg,)
        self.three_button.grid(row=0, column=0)

        self.five_button = Button(self.button_frame,
                                  text="5 Rounds",
                                  font=button_font, width=12,
                                  bg="#009900",
                                  fg=button_fg)
        self.five_button.grid(row=0, column=1,
                              padx=5, pady=5)

        self.ten_button = Button(self.button_frame,
                                 text="10 Rounds",
                                 font=button_font, width=12,
                                 bg="#000099",
                                 fg=button_fg)
        self.ten_button.grid(row=0, column=2,
                             padx=5, pady=5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    Menu()
    root.mainloop()
