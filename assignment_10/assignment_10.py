import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))

def save_file_as():
    save_file()

def change_format():
    color = colorchooser.askcolor()[1]
    text.configure(fg=color)

def show_custom_dialog():
    custom_dialog = tk.Toplevel(root)
    custom_dialog.title("Custom Dialog")

    label = tk.Label(custom_dialog, text="This is a custom dialog box.")
    label.pack()

    ok_button = tk.Button(custom_dialog, text="OK", command=custom_dialog.destroy)
    ok_button.pack()

def show_info_message():
    messagebox.showinfo("Information", "This is an information message.")

def show_error_message():
    messagebox.showerror("Error", "This is an error message.")

def ask_question():
    result = messagebox.askquestion("Question", "Do you want to continue?")
    if result == "yes":
        print("User wants to continue.")
    else:
        print("User doesn't want to continue.")

root = tk.Tk()
root.title("Text Editor")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)

format_menu = tk.Menu(menu)
menu.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Change Color", command=change_format)

custom_menu = tk.Menu(menu)
menu.add_cascade(label="Custom", menu=custom_menu)
custom_menu.add_command(label="Show Custom Dialog", command=show_custom_dialog)

message_menu = tk.Menu(menu)
menu.add_cascade(label="Messages", menu=message_menu)
message_menu.add_command(label="Show Info Message", command=show_info_message)
message_menu.add_command(label="Show Error Message", command=show_error_message)
message_menu.add_command(label="Ask Question", command=ask_question)

text = tk.Text(root)
text.pack()

root.mainloop()
