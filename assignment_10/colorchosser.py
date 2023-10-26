import tkinter as tk
from tkinter import colorchooser

def pick_color():
    color = colorchooser.askcolor()[1]
    text.configure(fg=color)

root = tk.Tk()
root.title("Color Picker")

color_button = tk.Button(root, text="Pick a Color", command=pick_color)
color_button.pack()

text = tk.Text(root)
text.pack()

root.mainloop()
