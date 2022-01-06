import os
from tkinter import Tk, Menu, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

edited = False
_open = None

root = Tk()

root.title("HexEdit")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

menu = Menu(root, tearoff=0)

file_dialog = filedialog.Open(master=root, title="Open a File", initialdir=os.getcwd(), filetypes=[("All Files", "*.*")])

text_out = ScrolledText(master=root)
text_out.grid(sticky="news")

text_out["state"] = "disabled"

def __open():
    text_out["state"] = "normal"

    text_out.delete("1.0", "end")

    _hex = open_file()

    if _hex:
        text_out.insert("1.0", _hex)

    text_out["state"] = "disabled"

def open_file():
    global _open

    path = file_dialog.show()

    if path:
        with open(path, "rb") as f:
            content = f.read(1024 * 4)

        _hex = ""

        for byte in content:
            _next_char = ("%x" % byte)

            if len(_next_char) == 1:
                _next_char = "0" + _next_char

            _hex += _next_char + " "

        _open = path

        return _hex

def save():
    if _open:
        pass # save

menu.add_command(label="Open", command=__open)
menu.add_command(label="Save", command=save)

root.config(menu=menu)

def _exit():
    if edited:
        warning = messagebox.askyesno("HexEdit", "You have unsaved changes. Are you sure you want to exit?", icon="warning")

        if warning:
            exit()
    else:
        exit()

root.protocol("WM_DELETE_WINDOW", _exit)

root.mainloop()