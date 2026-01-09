# TIC-TAC-TOE
import tkinter
import random
from tkinter import *

# --- Constants & Config ---
COLOR_BG = "#1E1E1E"
COLOR_BTN_NORMAL = "#333333"
COLOR_BTN_ACTIVE = "#555555"
COLOR_X = "#00E5FF"  # Cyan
COLOR_O = "#FF4081"  # Neon Pink
COLOR_WIN_BG = "#2E7D32" # Dark Green background for winner
COLOR_TIE = "#FFAB00" # Amber
FONT_MAIN = ("Verdana", 28, "bold")
FONT_TURN = ("Verdana", 16)
BTN_SIZE = 4 

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

# --- Game Logic ---

def next_turn(row, col):
    global turn, game_over

    if game_over:
        return

    if board[row][col]['text'] == "" and board[row][col] is not None:
        
        # Update board state
        board[row][col]['text'] = turn
        
        # Style the button based on player
        if turn == player[0]: # X
            board[row][col].config(fg=COLOR_X, activeforeground=COLOR_X)
        else: # O
            board[row][col].config(fg=COLOR_O, activeforeground=COLOR_O)

        if check_winner():
            label_turn.config(text=f"{turn} WINS!", fg=COLOR_X if turn == 'X' else COLOR_O)
            game_over = True
        elif check_tie():
            label_turn.config(text="IT'S A TIE!", fg=COLOR_TIE)
            game_over = True
        else:
            turn = player[1] if turn == player[0] else player[0]
            label_turn.config(text=f"{turn}'s TURN", fg="white")

def check_winner():
    # Check rows
    for row in range(3):
        if board[row][0]['text'] == board[row][1]['text'] == board[row][2]['text'] != "":
            highlight_winner([(row, 0), (row, 1), (row, 2)])
            return True

    # Check columns
    for col in range(3):
        if board[0][col]['text'] == board[1][col]['text'] == board[2][col]['text'] != "":
            highlight_winner([(0, col), (1, col), (2, col)])
            return True

    # Check diagonals
    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
        highlight_winner([(0, 0), (1, 1), (2, 2)])
        return True

    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
        highlight_winner([(0, 2), (1, 1), (2, 0)])
        return True

    return False

def check_tie():
    for row in range(3):
        for col in range(3):
            if board[row][col]['text'] == "":
                return False
    return True

def highlight_winner(coordinates):
    for row, col in coordinates:
        board[row][col].config(bg=COLOR_WIN_BG, relief="sunken")

def reset_game():
    global turn, game_over
    turn = random.choice(player)
    label_turn.config(text=f"{turn}'s TURN", fg="white")
    game_over = False

    for row in range(3):
        for col in range(3):
            board[row][col].config(text="", bg=COLOR_BTN_NORMAL, fg="white", relief="flat")

# --- Event Handlers ---
def on_enter(e):
    if not game_over and e.widget['text'] == "":
        e.widget['bg'] = COLOR_BTN_ACTIVE

def on_leave(e):
    if not game_over and e.widget['text'] == "":
        e.widget['bg'] = COLOR_BTN_NORMAL

# --- Setup UI ---

window = Tk()
window.title("TIC-TAC-TOE")
window.configure(bg=COLOR_BG)

# Set window size and center it
window_width = 500
window_height = 600
center_window(window, window_width, window_height)
window.resizable(False, False)

player = ["X", "O"]
turn = random.choice(player)
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
game_over = False

# Title / Turn Indicator
label_turn = Label(window, text=f"{turn}'s TURN", font=FONT_TURN, bg=COLOR_BG, fg="white", pady=20)
label_turn.pack()

# Game Board Frame
frame = Frame(window, bg=COLOR_BG)
frame.pack()

# Create Grid of Buttons
for row in range(3):
    for col in range(3):
        board[row][col] = Button(frame, text="", font=FONT_MAIN, width=BTN_SIZE, height=1,
                                 bg=COLOR_BTN_NORMAL, fg="white", activebackground=COLOR_BTN_ACTIVE,
                                 relief="flat", borderwidth=0, cursor="hand2",
                                 command=lambda r=row, c=col: next_turn(r, c))
        
        board[row][col].grid(row=row, column=col, padx=5, pady=5)
        
        # Bind hover effects
        board[row][col].bind("<Enter>", on_enter)
        board[row][col].bind("<Leave>", on_leave)

# Reset Button
reset_btn = Button(window, text="NEW GAME", font=("Verdana", 12), bg=COLOR_BTN_NORMAL, fg="white",
                   activebackground="#444", activeforeground="white", relief="flat",
                   command=reset_game, padx=20, pady=10, cursor="hand2")
reset_btn.pack(pady=30)


window.mainloop()
