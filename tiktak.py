import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

# Variables
player = "X"
board = [""] * 9

# Functions
def check_winner():
    # Winning combinations
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def on_click(i):
    global player
    if board[i] == "" and not check_winner():
        board[i] = player
        buttons[i].config(text=player)
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            else:
                messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_game()
        else:
            player = "O" if player == "X" else "X"

def reset_game():
    global board, player
    board = [""] * 9
    player = "X"
    for btn in buttons:
        btn.config(text="")

# GUI Buttons
buttons = []
for i in range(9):
    btn = tk.Button(root, text="", font=("Arial", 24), width=5, height=2, 
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Start GUI
root.mainloop()
