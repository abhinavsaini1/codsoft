import tkinter as tk
import random

# Game logic
def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    emojis = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}
    computer_choice = random.choice(options)
    result = ""

    if user_choice == computer_choice:
        result = f"It's a tie! We both picked {emojis[user_choice]} {user_choice}."
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = f"You win! {emojis[user_choice]} {user_choice} beats {emojis[computer_choice]} {computer_choice}."
        scores["user"] += 1
    else:
        result = f"I win! {emojis[computer_choice]} {computer_choice} beats {emojis[user_choice]} {user_choice}."
        scores["computer"] += 1

    result_label.config(text=f"You chose: {emojis[user_choice]} {user_choice}\nI chose: {emojis[computer_choice]} {computer_choice}\n{result}")
    score_label.config(text=f"Score → You: {scores['user']} | Me: {scores['computer']}")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("490x400")
root.resizable(False, False)

# Theme colors
bg_color = "#e3f2fd"  # Light blue
btn_color = "#90caf9"  # Button blue
btn_fg = "#0d47a1"    # Button text dark blue
lbl_color = "#42a5f5"  # Label blue
lbl_fg = "white"

root.configure(bg=bg_color)

scores = {"user": 0, "computer": 0}

title = tk.Label(root, text="Welcome to Rock, Paper, Scissors!", font=("Arial", 20, "bold"), bg=lbl_color, fg=lbl_fg)
title.pack(pady=10, fill="x")

instructions = tk.Label(root, text="Pick your move below. Can you beat me?", font=("Arial", 12), bg=bg_color, fg=btn_fg)
instructions.pack(pady=5)

button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="🪨 Rock", width=12, font=("Arial", 14),
                     command=lambda: play("Rock"), bg=btn_color, fg=btn_fg, activebackground=lbl_color, activeforeground=lbl_fg)
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="📄 Paper", width=12, font=("Arial", 14),
                      command=lambda: play("Paper"), bg=btn_color, fg=btn_fg, activebackground=lbl_color, activeforeground=lbl_fg)
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", width=12, font=("Arial", 14),
                         command=lambda: play("Scissors"), bg=btn_color, fg=btn_fg, activebackground=lbl_color, activeforeground=lbl_fg)
scissors_btn.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 14), justify="center", bg=bg_color, fg=btn_fg)
result_label.pack(pady=20)

score_label = tk.Label(root, text="Score → You: 0 | Me: 0", font=("Arial", 14, "bold"), bg=lbl_color, fg=lbl_fg)
score_label.pack(pady=5, fill="x")

exit_btn = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="#ef5350", fg="white", activebackground="#b71c1c", activeforeground="white")
exit_btn.pack(pady=20)

root.mainloop()