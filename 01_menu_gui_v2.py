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

        # if users press cross at tip, closes help and
        # 'refuses' help button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play))

        # variables used to work out statistics, when game ends ect
        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        # init set rounds placed and rounds won to 0
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_won = IntVar()
        self.rounds_won.set(0)

        # lists to hold user score/s and computer score/s
        # used to work out stats

        self.user_scores = []
        self.computer_scores = []

        # get all the colours for use in game
        self.all_colours = self.get_all_colours()

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        rounds_heading = "Choose - Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.quest_frame,
                                    text=rounds_heading,
                                    font=("Arial", "16", "bold"))
        self.choose_heading.grid(row=0)

        instructions = "Choose on of the colours below. When you choose" \
                       "a colour, the computer's choice and the results of" \
                       "the round will be revealed."
        self.instructions_label = Label(self.quest_frame, text=instructions,
                                        wraplength=350, justify="left")
        self.instructions_label.grid(row=1)

        # get colours for buttons for first round ...
        self.button_colours_list = self.get_round_colours()
        # print(self.button_colours_list)  # for testing purposes

        self.choice_frame = Frame(self.quest_frame)
        self.choice_frame.grid(row=2)

        # list to hold  references for control buttons
        # so that the text of the 'start over' button
        # con easily be configured when the game
        self.choice_button_ref = []

        for item in range(0, 6):
            self.choice_button = Button(self.choice_frame,
                                        width=15,
                                        command=lambda i=item: self.to_compare(self.button_colours_list[i]))

            self.choice_button_ref.append(self.choice_button)
            self.choice_button.grid(row=item // 3,
                                    column=item % 3,
                                    padx=5, pady=5)

            # add buttons to control list
            # self.choice_button_ref.append(self.make_)

        # display computer choice (after user has chosen a colour)
        self.com_choice_label = Label(self.quest_frame,
                                      text="Computers Choice will appear here",
                                      bg="#C0C0C0", width=51, )
        self.com_choice_label.grid(row=3, pady=10)

        # frame to include round results and next button
        self.rounds_frame = Frame(self.quest_frame)
        self.rounds_frame.grid(row=4, pady=5)

        self.rounds_results_label = Label(self.rounds_frame, text="Rounds 1: User: - \t Computer: - \t",
                                          width=32, bg="#FFF2CC",
                                          font=("Arial", 10),
                                          pady=5)
        self.rounds_results_label.grid(row=0, column=0, padx=5)

        self.next_button = Button(self.rounds_frame, text="Next Round",
                                  fg="#FFFFFF", bg="#008BFC",
                                  font=("Arial", 11, "bold"),
                                  width=10, state=DISABLED,
                                  command=self.new_round)
        self.next_button.grid(row=0, column=1)

        # large label to show overall gae results
        self.game_results_label = Label(self.quest_frame,
                                        text="Game Totals: User: - \t Computer - \t",
                                        bg="#FFF2CC", padx=10, pady=10,
                                        font=("Arial", "10"), width=42)
        self.game_results_label.grid(row=5, pady=5)

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

        # start game
        self.new_round()

    @staticmethod
    def get_all_colours():
        file = open("00_colour_list_hex_v3.csv", "r")
        var_all_colours = list(csv.reader(file, delimiter=","))
        file.close()

        # remove the first row (header values
        var_all_colours.pop(0)
        return var_all_colours

    def get_round_colours(self):
        rounds_colours_list = []
        colour_scores = []

        # Get six unique colours
        while len(rounds_colours_list) < 6:
            # choose item
            chosen_colour = random.choice(self.all_colours)
            index_chosen = self.all_colours.index(chosen_colour)

            # check score is not already in list
            if chosen_colour[2] not in colour_scores:
                # add item to rounds list
                rounds_colours_list.append(chosen_colour)

                # remove item from master list
                self.all_colours.pop(index_chosen)

        return rounds_colours_list

    def new_round(self):

        # disable next button (re-enable it at the end of the round)
        self.next_button.config(state=DISABLED)

        # empty button list so we can get new colours
        self.button_colours_list.clear()

        # get new colours bor buttons
        self.button_colours_list = self.get_round_colours()

        # set button bg, fg and text
        count = 0
        for item in self.choice_button_ref:
            item['fg'] = self.button_colours_list[count][2]
            item['bg'] = self.button_colours_list[count][0]
            item['text'] = self.button_colours_list[count][0]
            item['state'] = NORMAL
            count += 1

        # retrieve number of rounds wanted / played
        # and update heading.
        how_many = self.rounds_wanted.get()
        current_round = self.rounds_played.get()
        new_heading = "Choose - Round {} of " \
                      "{}".format(current_round + 1, how_many)
        self.choose_heading.config(text=new_heading)

    def to_compare(self, user_choice):

        how_many = self.rounds_wanted.get()

        # add one to number of rounds played
        current_round = self.rounds_played.get()
        current_round += 1
        self.rounds_played.set(current_round)

        # deactivate colour buttons!
        for item in self.choice_button_ref:
            item.config(state=DISABLED)

        # set up backgrounds colours...
        win_colour = "#D5E8D4"
        lose_colour = "#F8CECC"

        # retrieve user score, make it into an integer
        # and add to list for stats
        user_score_current = int(user_choice[1])
        self.user_scores.append(user_score_current)

        # remove user choice from button colours list
        to_remove = self.button_colours_list.index(user_choice)
        self.button_colours_list.pop(to_remove)

        # get computer choice and add to list for stats
        # when getting score, change it to an integer before
        # appending
        comp_choice = random.choice(self.button_colours_list)
        comp_score_current = int(comp_choice[1])

        self.computer_scores.append(comp_score_current)

        comp_announce = "The computer " \
                        "choice {}".format(comp_choice[0])

        self.com_choice_label.config(text=comp_announce,
                                     bg=comp_choice[0],
                                     fg=comp_choice[2])

        # get colours and show results!
        if user_score_current > comp_score_current:
            self.round_results_bg = win_colour
        else:
            self.round_results_bg = lose_colour

        round_outcome_txt = "Rounds {}: User {} \t" \
                            "Computer: {}".format(current_round,
                                                  user_score_current,
                                                  comp_score_current)
        self.rounds_results_label.config(bg=self.round_results_bg,
                                         text=round_outcome_txt)

        # get total scores for user and computer...
        user_total = sum(self.user_scores)
        comp_total = sum(self.computer_scores)

        # get colours and show results!
        if user_total > comp_total:
            self.game_results_label.config(bg=win_colour)
            status = "You Win!"
        else:
            self.game_results_label.config(bg=lose_colour)
            status = "You Lose!"

        game_outcome_txt = "Total Score: user {} \t" \
                           "Computer: {}".format(user_total,
                                                 comp_total)
        self.game_results_label.config(text=game_outcome_txt)

        if current_round == how_many:
            # change 'next' button to show overall
            # win / lose result and disable it
            self.next_button.config(state=DISABLED,
                                    text=status)

            # update 'start over button'
            start_over_button = self.control_button_ref[2]
            start_over_button['text'] = "Play Again"
            start_over_button['bg'] = "#009900"

            # change all colour button background to light grey
            for item in self.choice_button_ref:
                item['bg'] = "#C0C0C0"

        else:
            # enable next round button and update heading
            self.next_button.config(state=NORMAL)

    def to_do(self, action):
        if action == "get help":
            DisplayHelp(self)
        elif action == "get stats":
            DisplayStats(self)
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

    def __init__(self, partner):
        # set up dialogue box and background colour
        background = "#ffe6cc"
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
                                   text="stats / Info", bg=background,
                                   font=("Arial", "23", "bold"))
        self.stats_heading.grid(row=0)

        stats_text = "Your goal in this game is to beat the computer and you " \
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

        self.stats_text_label = Label(self.stats_frame, bg=background,
                                      text=stats_text, wraplength=350,
                                      justify="left")
        self.stats_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.stats_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_stats,
                                                     partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes stats dialogue (used by button and x at top of dialogue)
    def close_stats(self, partner):
        # Put stats button back tp normal...
        partner.to_stats_btn.config(state=NORMAL)
        self.stats_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    Menu()
    root.mainloop()
