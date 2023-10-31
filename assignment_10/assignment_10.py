import tkinter as tk
from tkinter import font
from tkinter import colorchooser

current_file = None  # To track the currently open file
modified = False  # To track if the text has been modified

def open_file(event=None):
    global current_file, modified
    file_path = tk.filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
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
    if current_file:
        with open(current_file, "w") as file:
            text = txt_edit.get(1.0, tk.END)
            file.write(text)
        modified = False

def change_font():
    font_obj = font.nametofont(txt_edit.cget("font"))
    font = tk.font.Font(root=txt_edit, family=font_obj.actual("family"), size=12)
    txt_edit.tag_configure("custom_font", font=font)
    txt_edit.tag_add("custom_font", txt_edit.index(tk.SEL_FIRST), txt_edit.index(tk.SEL_LAST))

def change_text_color():
    color = colorchooser.askcolor()[1]
    if color:
        txt_edit.tag_configure("custom_color", foreground=color)
        txt_edit.tag_add("custom_color", txt_edit.index(tk.SEL_FIRST), txt_edit.index(tk.SEL_LAST))

def save_file_as(event=None):
    global current_file, modified
    file_path = tk.filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file_path:
        return
    current_file = file_path
    with open(file_path, "w") as file:
        text = txt_edit.get(1.0, tk.END)
        file.write(text)
    window.title(f"Text Editor - {current_file}")
    modified = False

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
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As...", command=save_file_as, accelerator="Ctrl+Shift+S")
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
