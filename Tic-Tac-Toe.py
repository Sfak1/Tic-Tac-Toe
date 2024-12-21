from tkinter import *
import random

# Functions
def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and not check_winner():
        buttons[row][column]['text'] = player

        if check_winner():
            label.config(text="You win!" if mode == "1-player" else f"{player} wins!")
            scores[player] += 1
            update_scores()
        elif not empty_spaces():
            label.config(text="It's a Tie!")
        else:
            if mode == "1-player":
                computer_turn()
            else:
                switch_player()

def computer_turn():
    global player

    # Randomly choose an empty space for the computer
    empty = [(row, col) for row in range(3) for col in range(3) if buttons[row][col]['text'] == ""]
    if empty:
        row, col = random.choice(empty)
        buttons[row][col]['text'] = "O"

        if check_winner():
            label.config(text="Computer wins!")
            scores["O"] += 1
            update_scores()
        elif not empty_spaces():
            label.config(text="It's a Tie!")

def switch_player():
    global player
    player = "X" if player == "O" else "O"
    label.config(text=f"{player}'s Turn")

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            highlight_winner([(row, 0), (row, 1), (row, 2)])
            return True

    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            highlight_winner([(0, col), (1, col), (2, col)])
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        highlight_winner([(0, 0), (1, 1), (2, 2)])
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        highlight_winner([(0, 2), (1, 1), (2, 0)])
        return True

    return False

def highlight_winner(positions):
    for row, col in positions:
        buttons[row][col].config(bg="green")

def empty_spaces():
    return any(buttons[row][col]['text'] == "" for row in range(3) for col in range(3))

def new_game():
    global player
    player = "X"  # Player always starts as X
    label.config(text=f"{player}'s Turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#F0F0F0")

def update_scores():
    score_label.config(text=f"X: {scores['X']} | O: {scores['O']}")

def start_game(selected_mode):
    global mode, players, player
    mode = selected_mode
    players = ["X", "O"]
    player = "X"  # Human player always starts as X

    # Clear the start screen and show the game
    start_frame.pack_forget()
    game_frame.pack()

    label.config(text="Your Turn!" if mode == "1-player" else f"{player}'s Turn")

# Setup GUI
window = Tk()
window.title("Tic-Tac-Toe")
# Center the window on the screen
window_width = 600
window_height = 800
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width // 2) - (window_width // 2)
y_coordinate = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Variables
mode = ""
players = []
player = ""
scores = {"X": 0, "O": 0}

# Start Screen
start_frame = Frame(window, width=400, height=500)
start_frame.pack_propagate(False)  # Prevent resizing
start_frame.pack()

Label(start_frame, text="Tic-Tac-Toe", font=('consolas', 30)).pack(pady=20)

Button(start_frame, text="1 Player (Solo)", font=('consolas', 20), command=lambda: start_game("1-player"), bg="lightblue").pack(pady=10)
Button(start_frame, text="2 Players", font=('consolas', 20), command=lambda: start_game("2-players"), bg="orange").pack(pady=10)

# Game Screen
game_frame = Frame(window)

label = Label(game_frame, text="", font=('consolas', 30), bg="lightblue", width=20)
label.pack(side="top", pady=10)

frame = Frame(game_frame)
frame.pack()

buttons = [[None for _ in range(3)] for _ in range(3)]
for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                   command=lambda row=row, col=col: next_turn(row, col))
        buttons[row][col].grid(row=row, column=col, padx=5, pady=5)

score_label = Label(game_frame, text="X: 0 | O: 0", font=('consolas', 20), bg="lightgrey", width=20)
score_label.pack(side="top", pady=10)

reset_button = Button(game_frame, text="Restart Game", font=('consolas', 20), command=new_game, bg="orange")
reset_button.pack(side="top", pady=10)

# Start the main loop
window.mainloop()
