import tkinter


class MainMenu:
    def __init__(self, master):
        self.master = master
        master.title("Main Menu")

        # Create menu bar
        self.menu_bar = tkinter.Menu(master)
        master.config(menu=self.menu_bar)

        # Create game menu
        self.game_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.game_menu.add_command(label="Play game", command=self.play_game)
        self.menu_bar.add_cascade(label="Game", menu=self.game_menu)

        # Create settings menu
        self.settings_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.settings_menu.add_command(label="Change settings", command=self.change_settings)
        self.menu_bar.add_cascade(label="Settings", menu=self.settings_menu)

    def play_game(self):
        # self.hide_menu()
        game_window = tkinter.Toplevel(self.master)
        game = TicTacToe(game_window)

    def change_settings(self):
        self.hide_menu()
        settings_window = tkinter.Toplevel(self.master)
        # add widgets for settings window
        settings_label = tkinter.Label(settings_window, text="Settings Window")
        settings_label.pack()

    def hide_menu(self):
        self.master.withdraw()


class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe")

        # Creating buttons
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tkinter.Button(master, text="", width=5, height=2,
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
                self.start_new_game()
            elif self.check_tie():
                self.status_label.config(text="TIE")
                for button in self.buttons:
                    button.config(state=tkinter.DISABLED)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"{self.current_player}'S TURN")

    def check_win(self):
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

    def start_new_game(self):
        self.current_player = "X"
        self.board = [" " for i in range(9)]
        for button in self.buttons:
            button.config(text="", state=tkinter.NORMAL)
        self.status_label.config(text="Player X's turn")

    def check_tie(self):
        return all(x != " " for x in self.board)


if __name__ == '__main__':
    x: int = int(1)
    root = tkinter.Tk()
    menu = MainMenu(root)
    root.mainloop()
