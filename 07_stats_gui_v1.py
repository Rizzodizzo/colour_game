from tkinter import *
from functools import partial
import csv
import random


class Menu:

    def __init__(self):
        # invoke play class with three rounds for testing purposes.
        self.to_play(3)

    def to_play(self, num_rounds):
        Play(num_rounds)

        # hide Menu
        root.withdraw()


class Play:

    def __init__(self, how_many):
        self.play_box = Toplevel()

        # lists of user and computer scores
        # used to work out stats
        self.users_scores = [20, 14, 14, 13, 14, 11, 20, 10, 20, 11]
        self.computer_scores = [12, 4, 6, 20, 20, 14, 10, 14, 16, 22]

        # if users press cross at tip, closes help and
        # 'refuses' help button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play))

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        self.control_frame = Frame(self.quest_frame)
        self.control_frame.grid(row=6)

        control_buttons = [
            ["#CC6600", "Help", "get help"],
            ["#004C99", "Statistics", "get stats"],
            ["#808080", "Start Over", "start over"]
        ]

        # list to hold  references for control buttons
        # so that the text of the 'start over' button
        # con easily be configured when the game
        self.control_button_ref = []

        for item in range(0, 3):
            self.make_control_button = Button(self.control_frame,
                                              fg="#FFFFFF",
                                              bg=control_buttons[item][0],
                                              text=control_buttons[item][1],
                                              width=11, font=("Arial", 12, "bold"),
                                              command=lambda i=item: self.to_do(control_buttons[i][2]))
            self.make_control_button.grid(row=0, column=item, padx=5, pady=5)

            # add buttons to control list
            self.control_button_ref.append(self.make_control_button)

        # disable help button
        self.to_help_btn = self.control_button_ref[0]
        self.to_stats_btn = self.control_button_ref[1]

    def to_do(self, action):
        if action == "get help":
            DisplayHelp(self)
        elif action == "get stats":
            DisplayStats(self, self.users_scores, self.computer_scores)
        else:
            self.close_play()

    def close_play(self):
        # reshow menu
        # game / allow new game to start
        root.deiconify()
        self.play_box.destroy()


class DisplayHelp:

    def __init__(self, partner):
        # set up dialogue box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_btn.config(state=DISABLED)

        # if users press cross at top, closes help and
        # 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200,
                                bg=background)
        self.help_frame.grid()

        self.help_heading = Label(self.help_frame,
                                  text="Help / Info", bg=background,
                                  font=("Arial", "23", "bold"))
        self.help_heading.grid(row=0)

        help_text = "Your goal in this game is to beat the computer and you " \
                    "have an advantage - you get to choose your colour first. " \
                    "The points associated with the colour are based on the colours " \
                    "hex code." \
                    "\n\n" \
                    "THe higher the value of the colour, the greater your score. To " \
                    "see you statistics press the 'Statistics' button. \n\n" \
                    "Win the game by scoring more than the computer overall. " \
                    "Don't be discouraged if you dont win every round, it's " \
                    "your overall score that counts.\n\n" \
                    "Good luck! Choose carefully."

        self.help_text_label = Label(self.help_frame, bg=background,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help,
                                                     partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes help dialogue (used by button and x at top of dialogue)
    def close_help(self, partner):
        # Put help button back tp normal...
        partner.to_help_btn.config(state=NORMAL)
        self.help_box.destroy()


class DisplayStats:

    def __init__(self, partner, user_scores, computer_scores):
        # set up dialogue box and background colour
        background = "#DAE8FC"
        self.stats_box = Toplevel()

        # disable stats button
        partner.to_stats_btn.config(state=DISABLED)

        # if users press cross at top, closes stats and
        # 'releases' stats button
        self.stats_box.protocol('WM_DELETE_WINDOW',
                                partial(self.close_stats, partner))

        self.stats_frame = Frame(self.stats_box, width=300, height=200,
                                 bg=background)
        self.stats_frame.grid()

        self.stats_heading = Label(self.stats_frame,
                                   text="Statistics", bg=background,
                                   font=("Arial", "14", "bold"))
        self.stats_heading.grid(row=0)

        stats_text = "Here are your game statistics"

        self.stats_text_label = Label(self.stats_frame, bg=background,
                                      text=stats_text, justify="left")
        self.stats_text_label.grid(row=1, padx=10)

        # frame to hold statistics 'table'
        self.data_frame = Frame(self.stats_frame, bg=background,
                                borderwidth=1, relief="solid")
        self.data_frame.grid(row=2, padx=10, pady=10)

        self.user_stats = self.get_stats(user_scores, "User")
        self.comp_stats = self.get_stats(computer_scores, "Computer")

        # background formatting for heading, odd and even rows
        head_back = "#FFFFFF"
        odd_rows = "#C9D6E8"
        even_rows = background

        row_names = ["", "Total", "Best Score", "Worst Score", "Average Score"]
        row_formats = [head_back, odd_rows, even_rows, odd_rows, even_rows]

        # data for labels (one label / sublist)
        all_labels = []

        count = 0
        for item in range(0, len(self.user_stats)):
            all_labels.append([row_names[item], row_formats[count]])
            all_labels.append([self.user_stats[item], row_formats[count]])
            all_labels.append([self.comp_stats[item], row_formats[count]])
            count += 1

        # create labels based on list above
        for item in range(0, len(all_labels)):
            self.data_label = Label(self.data_frame, text=all_labels[item][0],
                                    bg=all_labels[item][1],
                                    width="10", height="2", padx=5)

            self.data_label.grid(row=item // 3,
                                 column=item % 3,
                                 padx=0, pady=0)

        # dismiss button
        self.dismiss_button = Button(self.stats_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_stats,
                                                     partner))
        self.dismiss_button.grid(row=3, padx=10, pady=10)

    # closes stats dialogue (used by button and x at top of dialogue)
    def close_stats(self, partner):
        # Put stats button back tp normal...
        partner.to_stats_btn.config(state=NORMAL)
        self.stats_box.destroy()

    # calculate stats and column
    # heading at first item
    @staticmethod
    def get_stats(score_list, entity):
        total_score = sum(score_list)
        best_score = max(score_list)
        worst_score = min(score_list)
        average = total_score / len(score_list)

        return [entity, total_score, best_score, worst_score, average]


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    Menu()
    root.mainloop()
