import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    comp_choice = random.choice(choices)

    user_label.config(text=f"You: {user_choice}")
    comp_label.config(text=f"Computer: {comp_choice}")

    if user_choice == comp_choice:
        result = "Draw!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"

    result_label.config(text=result)

def reset():
    user_label.config(text="You: ")
    comp_label.config(text="Computer: ")
    result_label.config(text="")


root = tk.Tk()
root.title("Rock Paper Scissors")


for c in choices:
    tk.Button(root, text=c, width=10, command=lambda c=c: play(c)).pack(pady=2)


user_label = tk.Label(root, text="You: ")
user_label.pack()

comp_label = tk.Label(root, text="Computer: ")
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)


tk.Button(root, text="Reset", command=reset).pack()

root.mainloop()