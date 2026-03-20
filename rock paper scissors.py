import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user):
    comp = random.choice(choices)
    user_lbl.config(text="You: " + user)
    comp_lbl.config(text="Computer: " + comp)

    if user == comp:
        result = "Tie!"
    elif (user, comp) in [("Rock","Scissors"), ("Paper","Rock"), ("Scissors","Paper")]:
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_lbl.config(text=result)

def reset():
    user_lbl.config(text="You:")
    comp_lbl.config(text="Computer:")
    result_lbl.config(text="")

root = tk.Tk()
root.title("RPS")

user_lbl = tk.Label(root, text="You:")
comp_lbl = tk.Label(root, text="Computer:")
result_lbl = tk.Label(root, font=("Arial", 14))

user_lbl.pack()
comp_lbl.pack()
result_lbl.pack()

for c in choices:
    tk.Button(root, text=c, width=10, command=lambda x=c: play(x)).pack(pady=2)

tk.Button(root, text="Reset", command=reset).pack(pady=5)

root.mainloop()