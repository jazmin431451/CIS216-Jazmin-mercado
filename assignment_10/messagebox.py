import tkinter as tk
from tkinter import messagebox

def show_info():
    messagebox.showinfo("Information", "This is an information message.")

def show_error():
    messagebox.showerror("Error", "This is an error message.")

def ask_question():
    result = messagebox.askquestion("Question", "Do you want to continue?")
    if result == "yes":
        print("User wants to continue.")
    else:
        print("User doesn't want to continue.")

root = tk.Tk()
root.title("Message Boxes")

info_button = tk.Button(root, text="Show Info", command=show_info)
info_button.pack()

error_button = tk.Button(root, text="Show Error", command=show_error)
error_button.pack()

question_button = tk.Button(root, text="Ask Question", command=ask_question)
question_button.pack()

root.mainloop()
