import tkinter as tk
from tkinter import font
from tkinter import colorchooser
from tkinter import messagebox, filedialog
from tkinter.simpledialog import askstring

current_file = None  # To track the currently open file
modified = False  # To track if the text has been modified

def open_file(event=None):
    global current_file, modified
    if modified:
        save_prompt = messagebox.askyesnocancel("Save Changes", "Do you want to save the changes before opening a new file?")
        if save_prompt is None:
            return 
        if save_prompt:
            save_file()
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return
    current_file = file_path
    with open(file_path, "r") as file:
        text = file.read()
        txt_edit.delete(1.0, tk.END)
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor - {current_file}")
    modified = False

def save_file(event=None):
    global current_file, modified
    if not current_file:
        save_file_as()
        return
    with open(current_file, "w") as file:
        text = txt_edit.get(1.0, tk.END)
        file.write(text)
    window.title(f"Text Editor - {current_file}")
    modified = False

def save_file_as(event=None):
    global current_file, modified
    file_path = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return
    current_file = file_path
    with open(file_path, "w") as file:
        text = txt_edit.get(1.0, tk.END)
        file.write(text)
    window.title(f"Text Editor - {current_file}")
    modified = False

def change_font():
    font_name = askstring("Font Selection", "Enter font name (e.g., Arial):")
    if font_name:
        txt_edit.tag_configure("custom_font", font=(font_name, 12))
        txt_edit.tag_add("custom_font", txt_edit.index(tk.SEL_FIRST), txt_edit.index(tk.SEL_LAST))

def change_text_color():
    color = colorchooser.askcolor()[1]
    if color:
        txt_edit.tag_configure("custom_color", foreground=color)
        txt_edit.tag_add("custom_color", txt_edit.index(tk.SEL_FIRST), txt_edit.index(tk.SEL_LAST))



def text_modified(event=None):
    global modified
    modified = True

window = tk.Tk()
window.title("Text Editor")

window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

txt_edit = tk.Text(window)
txt_edit.grid(row=0, column=1, sticky="nsew")
txt_edit.bind("<Key>", text_modified)

scrollbar = tk.Scrollbar(window, command=txt_edit.yview)
scrollbar.grid(row=0, column=2, sticky="ns")
txt_edit.config(yscrollcommand=scrollbar.set)

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open (Ctrl+O)", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save (Ctrl+S)", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As (Ctrl+Shift+S)", command=save_file_as, accelerator="Ctrl+Shift+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)

format_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Format", menu=format_menu)
format_menu.add_command(label="Change Font", command=change_font)
format_menu.add_command(label="Change Text Color", command=change_text_color)

window.bind("<Control-o>", open_file)
window.bind("<Control-s>", save_file)
window.bind("<Control-S>", save_file_as)

window.protocol("WM_DELETE_WINDOW", window.quit)

window.mainloop()
