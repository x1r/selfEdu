import random
import tkinter


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.bot_side = None
        self.bot_difficulty = 1
        master.title("Tic-Tac-Toe")
        # Creating buttons
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tkinter.Button(master, text="", width=10, height=4,
                                        command=lambda row=i, col=j: self.button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

        # Starting player
        self.current_player = "X"

        # Creating board
        self.board = [" " for i in range(9)]

        # Widget for displaying player's turn
        self.status_label = tkinter.Label(master, text="Player X's turn")
        self.status_label.grid(row=3, column=0, columnspan=3)

        # Scoreboard
        self.scores = {"X": 0, "O": 0}
        self.score_label = tkinter.Label(master, text=f"Scores: X - {self.scores['X']}, O - {self.scores['O']}'")
        self.score_label.grid(row=4, column=0, columnspan=3)

        # New game button
        self.new_game_button = tkinter.Button(master, command=self.start_new_game, text="START NEW GAME")
        self.new_game_button.grid(row=5, column=0, columnspan=3)

        # Create menu bar
        self.menu_bar = tkinter.Menu(master)
        master.config(menu=self.menu_bar)

        # Create game menu
        self.game_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.game_menu.add_command(label="Play with a friend", command=self.play_friend)
        self.game_menu.add_command(label="Play with a computer", command=self.play_bot)
        self.menu_bar.add_cascade(label="Game", menu=self.game_menu)

        # Create settings menu
        self.settings_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.settings_menu.add_command(label="Change settings", command=self.change_settings)
        self.menu_bar.add_cascade(label="Settings", menu=self.settings_menu)
        self.start_new_game()

    def play_friend(self):
        self.bot_side = None
        self.start_new_game()

    def play_bot(self):
        choose_side_window = tkinter.Toplevel(self.master)
        choose_side_label = tkinter.Label(choose_side_window, text="Choose your side")
        choose_side_label.pack()
        choose_side_button_x = tkinter.Button(choose_side_window, text="X",
                                              command=lambda: self.close_choose_side_window(choose_side_window, "X"))
        choose_side_button_x.pack()
        choose_side_button_o = tkinter.Button(choose_side_window, text="O",
                                              command=lambda: self.close_choose_side_window(choose_side_window, "O"))
        choose_side_button_o.pack()

    def close_choose_side_window(self, choose_side_window, side):
        choose_side_window.destroy()
        if side == "X":
            bot = "O"
        else:
            bot = "X"
        self.start_new_game(player=side, bot=bot)

    def bot_move(self):
        # Check if bot's turn
        if self.bot_side != self.current_player:
            return

        # Minimax algorithm
        def minimax(board, depth, is_maximizing):
            if self.check_win(board):
                return 1 if is_maximizing else -1
            if self.check_win(board, self.bot_side):
                return 1 if is_maximizing else -1
            if " " not in board:
                return 0

            if is_maximizing:
                best_score = -float("inf")
                for i in range(9):
                    if board[i] == " ":
                        board[i] = self.bot_side
                        score = minimax(board, depth + 1, False)
                        board[i] = " "
                        best_score = max(best_score, score)
                return best_score
            else:
                # Choose the move that minimizes the score
                best_score = float("inf")
                for i in range(9):
                    if board[i] == " ":
                        board[i] = "O" if self.bot_side == "X" else "X"
                        score = minimax(board, depth + 1, True)
                        board[i] = " "
                        best_score = min(best_score, score)
                return best_score

        best_move = None
        if self.bot_difficulty > 0:
            best_score = -float("inf")
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = self.bot_side
                    score = minimax(self.board, self.bot_difficulty, False)
                    self.board[i] = " "
                    if score > best_score:
                        best_score = score
                        best_move = i
        else:
            best_move = random.choice([i for i in range(9) if self.board[i] == " "])

        # Make the move
        self.board[best_move] = self.bot_side
        self.buttons[best_move].config(text=self.bot_side)

        # Check for win or draw
        if self.check_win():
            self.scores[self.bot_side] += 1
            self.status_label.config(text=f"Player {self.bot_side} WINS!")
            self.score_label.config(text=f"SCORES: X - {self.scores['X']}, O - {self.scores['O']}")
            for button in self.buttons:
                button.config(state=tkinter.DISABLED)
            self.start_new_game()
        elif " " not in self.board:
            self.status_label.config(text="DRAW!")
            for button in self.buttons:
                button.config(state=tkinter.DISABLED)
            self.start_new_game()
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(text=f"{self.current_player}'S TURN")

    def button_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_win():
                self.scores[self.current_player] += 1
                self.status_label.config(text=f"Player {self.current_player} WINS!")
                self.score_label.config(text=f"SCORES: X - {self.scores['X']}, O - {self.scores['O']}")
                for button in self.buttons:
                    button.config(state=tkinter.DISABLED)
                self.start_new_game(player=self.current_player, bot=self.bot_side)
            elif self.check_tie():
                self.status_label.config(text="TIE")
                for button in self.buttons:
                    button.config(state=tkinter.DISABLED)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"{self.current_player}'S TURN")
                self.bot_move()

    def check_win(self, board=None, player=None):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != " ":
                return True
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return True
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True
        return False

    def start_new_game(self, player=None, bot=None):
        # Reset buttons and board
        for button in self.buttons:
            button.config(text="")
            button.config(state=tkinter.NORMAL)
        self.board = [" " for i in range(9)]

        # Setting starting player
        if player:
            self.current_player = player
        else:
            self.current_player = "X"

        # Setting bot side
        self.bot_side = bot

        # Update status label
        self.status_label.config(text=f"Player {self.current_player}'S TURN")

    def check_tie(self):
        return all(x != " " for x in self.board)

    def change_settings(self):
        settings_window = tkinter.Toplevel(self.master)
        settings_window.title("Settings")

        # add label for bot difficulty
        bot_difficulty_label = tkinter.Label(settings_window, text="Bot difficulty:")
        bot_difficulty_label.pack()

        # create a variable to store the selected bot difficulty
        bot_difficulty = tkinter.StringVar()
        bot_difficulty.set("Random moves")

        # create a drop-down menu to select the bot difficulty
        bot_difficulty_menu = tkinter.OptionMenu(settings_window, bot_difficulty, "Random moves", "Easy", "Medium",
                                                 "Hard")
        bot_difficulty_menu.pack()

        def change_difficulty(difficulty):
            if difficulty == "Random moves":
                self.bot_difficulty = 0
            elif difficulty == "Easy":
                self.bot_difficulty = 1
            elif difficulty == "Medium":
                self.bot_difficulty = 2
            elif difficulty == "Hard":
                self.bot_difficulty = 3
            settings_window.destroy()
            return

        # add a button to save the settings
        save_button = tkinter.Button(settings_window, text="Save",
                                     command=lambda: change_difficulty(bot_difficulty.get()))
        save_button.pack()


if __name__ == "__main__":
    root = tkinter.Tk()
    game = TicTacToe(root)
    root.mainloop()
