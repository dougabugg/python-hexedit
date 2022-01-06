import os
from tkinter import Tk, Menu, filedialog
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title("HexEdit")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

menu = Menu(root, tearoff=0)

file_dialog = filedialog.Open(master=root, title="Open a File", initialdir=os.getcwd(), filetypes=[("All Files", "*.*")])

text_out = ScrolledText(master=root)
text_out.grid(sticky="news")
text_out["state"] = "disabled"

def _open():
    text_out["state"] = "normal"
    text_out.delete("1.0", "end")
    _hex = open_file()
    text_out.insert("1.0", _hex)
    text_out["state"] = "disabled"

def open_file():
    path = file_dialog.show()

    if path:
        with open(path, "rb") as f:
            content = f.read(1024 * 4)

        _hex = ""

        for byte in content:
            _next_char = ('%x' % byte)
            if len(_next_char) == 1:
                _next_char = "0" + _next_char
            _hex += _next_char + " "

        return _hex

    return "No File Selected."

def save():
    pass

menu.add_command(label="Open", command=_open)
menu.add_command(label="Save", command=save)

root.config(menu=menu)

root.mainloop()