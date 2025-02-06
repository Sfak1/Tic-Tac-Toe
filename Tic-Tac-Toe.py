from tkinter import *
import random

# Initialize game variables
def initialize_game():
    global player, scores, mode
    player = "X"  # X always starts
    scores = {"X": 0, "O": 0}
    mode = ""

def handle_turn(row, col):
    global player
    if buttons[row][col]['text'] == "" and not check_winner():
        buttons[row][col]['text'] = player
        if check_winner():
            label.config(text="You win!" if mode == "1-player" else f"{player} wins!")
            scores[player] += 1
            update_scores()
        elif not available_moves():
            label.config(text="It's a Tie!")
        else:
            if mode == "1-player":
                computer_move()
            else:
                switch_player()

def computer_move():
    empty_cells = [(r, c) for r in range(3) for c in range(3) if buttons[r][c]['text'] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        buttons[row][col]['text'] = "O"
        if check_winner():
            label.config(text="Computer wins!")
            scores["O"] += 1
            update_scores()
        elif not available_moves():
            label.config(text="It's a Tie!")
        #else:
            #label.config(text="Your Turn!")

def switch_player():
    global player
    player = "X" if player == "O" else "O"
    label.config(text=f"{player}'s Turn")
    
# Check if a player has won
def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            highlight_winner([(i, 0), (i, 1), (i, 2)])
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            highlight_winner([(0, i), (1, i), (2, i)])
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        highlight_winner([(0, 0), (1, 1), (2, 2)])
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        highlight_winner([(0, 2), (1, 1), (2, 0)])
        return True
    return False

def highlight_winner(positions):
    for r, c in positions:
        buttons[r][c].config(bg="green")

def available_moves():
    return any(buttons[r][c]['text'] == "" for r in range(3) for c in range(3))

def reset_board():
    global player
    player = "X"
    label.config(text=f"{player}'s Turn")
    for r in range(3):
        for c in range(3):
            buttons[r][c].config(text="", bg="#F0F0F0")

def update_scores():
    score_label.config(text=f"X: {scores['X']} | O: {scores['O']}")

def start_game(selected_mode):
    global mode, player
    mode = selected_mode
    player = "X"
    start_frame.pack_forget()
    game_frame.pack()
    label.config(text=f"{player}'s Turn")

# GUI Setup
window = Tk()
window.title("Tic-Tac-Toe")
window.geometry("600x800")
initialize_game()

start_frame = Frame(window)
start_frame.pack()
Label(start_frame, text="Tic-Tac-Toe", font=('consolas', 30)).pack(pady=20)
Button(start_frame, text="1 Player(Solo)", font=('consolas', 20), command=lambda: start_game("1-player"), bg="lightblue").pack(pady=10)
Button(start_frame, text="2 Players", font=('consolas', 20), command=lambda: start_game("2-players"), bg="orange").pack(pady=10)

game_frame = Frame(window)
label = Label(game_frame, text="", font=('consolas', 30), bg="lightblue")
label.pack(side="top", pady=10)
frame = Frame(game_frame)
frame.pack()
buttons = [[Button(frame, text="", font=('consolas', 40), width=5, height=2, command=lambda r=r, c=c: handle_turn(r, c)) for c in range(3)] for r in range(3)]
for r in range(3):
    for c in range(3):
        buttons[r][c].grid(row=r, column=c, padx=5, pady=5)
score_label = Label(game_frame, text="X: 0 | O: 0", font=('consolas', 20), bg="lightgrey")
score_label.pack()
Button(game_frame, text="Restart", font=('consolas', 20), command=reset_board, bg="orange").pack()

window.mainloop()
