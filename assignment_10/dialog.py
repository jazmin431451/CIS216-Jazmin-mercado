import tkinter as tk

def show_custom_dialog():
    custom_dialog = tk.Toplevel(root)
    custom_dialog.title("Custom Dialog")

    label = tk.Label(custom_dialog, text="This is a custom dialog box.")
    label.pack()

    ok_button = tk.Button(custom_dialog, text="OK", command=custom_dialog.destroy)
    ok_button.pack()

root = tk.Tk()
root.title("Custom Dialog Example")

custom_button = tk.Button(root, text="Show Custom Dialog", command=show_custom_dialog)
custom_button.pack()

root.mainloop()
