#TIC-TAC-TOE
import tkinter
import random
from tkinter import *
from tkinter import ttk

#-------------------------------------------------------------

def next_turn(x, y, button):
    global turn, game_over
    
    if game_over:
        return
    
    if board[x][y] == 0:
        board[x][y] = turn
        button.config(text=turn, fg='red' if turn == 'X' else 'blue')
        
        if win():
            label_turn.config(text=turn + " WINS!", fg='green')
            game_over = True
            return
        
        # Check for tie
        if is_tie():
            label_turn.config(text="IT'S A TIE!", fg='orange')
            game_over = True
            return
        
        # Switch turns
        turn = "O" if turn == "X" else "X"
        label_turn.config(text=turn + " TURN")

def is_tie():
    for row in board:
        if 0 in row:
            return False
    return True

def win():
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            return True
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            return True
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return True
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return True
    
    return False

def reset():
    global turn, board, game_over
    
    turn = random.choice(player)
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    game_over = False
    
    label_turn.config(text=turn + " TURN", fg='black')
    
    # Reset all buttons
    for row in buttons:
        for button in row:
            button.config(text="")

#-------------------------------------------------------------

window = Tk()
window.title("TIC-TAC-TOE")
window.geometry("225x315")
window.resizable(False, False)

player = ["X", "O"]
turn = random.choice(player)
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
game_over = False

label_turn = Label(window, text=turn + " TURN", font=("Trebuchet MS", 20), bg='#ADD8E6')
label_turn.pack()

bu_reset = Button(window, text="RESET", bg='#ADD8E6', height=2, width=5, command=reset)
bu_reset.pack()

frame = Frame(window)
frame.pack()

#--------------------------------------------------------------

# Create buttons and store them in a 2D list
buttons = []
for i in range(3):
    button_row = []
    for j in range(3):
        btn = Button(frame, text="", height=2, width=6, font=("Calibri", 16),
                     command=lambda x=i, y=j: next_turn(x, y, buttons[x][y]))
        btn.grid(row=i, column=j)
        button_row.append(btn)
    buttons.append(button_row)

window.mainloop()