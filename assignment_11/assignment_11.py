import tkinter as tk
from tkinter import font
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox

class TextEditor(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.current_file = None
        self.modified = False

        self.title("Text Editor")
        self.geometry("800x600")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.txt_edit = tk.Text(self)
        self.txt_edit.grid(row=0, column=1, sticky="nsew")
        self.txt_edit.bind("<Key>", self.text_modified)

        scrollbar = tk.Scrollbar(self, command=self.txt_edit.yview)
        scrollbar.grid(row=0, column=2, sticky="ns")
        self.txt_edit.config(yscrollcommand=scrollbar.set)

        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        self.create_menu()
        self.create_bindings()
        self.protocol("WM_DELETE_WINDOW", self.quit)

    def create_menu(self):
        self.file_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open (Ctrl+O)", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save (Ctrl+S)", command=self.save_file, accelerator="Ctrl+S")
        self.file_menu.add_command(label="Save As (Ctrl+Shift+S)", command=self.save_file_as, accelerator="Ctrl+Shift+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)

        self.format_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label="Change Font", command=self.change_font)
        self.format_menu.add_command(label="Change Text Color", command=self.change_text_color)

    def create_bindings(self):
        self.bind("<Control-o>", self.open_file)
        self.bind("<Control-s>", self.save_file)
        self.bind("<Control-S>", self.save_file_as)

    def open_file(self, event=None):
        global current_file, modified
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not file_path:
            return
        current_file = file_path
        with open(file_path, "r") as file:
            text = file.read()
            self.txt_edit.delete(1.0, tk.END)
            self.txt_edit.insert(tk.END, text)
        self.title(f"Text Editor - {current_file}")
        self.modified = False

    def save_file(self, event=None):
        global current_file, modified
        if current_file:
            with open(current_file, "w") as file:
                text = self.txt_edit.get(1.0, tk.END)
                file.write(text)
            self.modified = False

    def change_font(self):
        font_selection = simpledialog.askstring("Font Selection", "Enter the font (e.g., Arial 12):")
        if font_selection:
            try:
                font_obj = font.Font(root=self.txt_edit, family=font_selection.split()[0], size=int(font_selection.split()[1]))
                self.txt_edit.configure(font=font_obj)
            except:
                messagebox.showerror("Error", "Invalid font format. Please use 'FontName Size'.")

    def change_text_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.txt_edit.tag_configure("custom_color", foreground=color)
            self.txt_edit.tag_add("custom_color", self.txt_edit.index(tk.SEL_FIRST), self.txt_edit.index(tk.SEL_LAST))

    def save_file_as(self, event=None):
        global current_file, modified
        file_path = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not file_path:
            return
        current_file = file_path
        with open(file_path, "w") as file:
            text = self.txt_edit.get(1.0, tk.END)
            file.write(text)
        self.title(f"Text Editor - {current_file}")
        self.modified = False

    def text_modified(self, event=None):
        self.modified = True

if __name__ == "__main__":
    app = TextEditor()
    app.mainloop()
