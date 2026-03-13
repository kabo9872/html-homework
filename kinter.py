from tkinter import *

window = Tk()
window.title("Button example")
window.geometry("300x200")

def change_text():
    label.config(text="Button Clicked!")

label = Label(window, text="Welcom user", font=("Arial", 14))
label.pack(pady=20)

button = Button(window, text="Click Me", command=change_text)
button.pack()

window.mainloop()