import os
from tkinter import Tk, Menu, filedialog, ttk
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title("HexEdit")
root.resizable(False, False)

menu = Menu(root, tearoff=0)

file_dialog = filedialog.Open(master=root, title="Open a File", initialdir=os.getcwd(), filetypes=[("All Files", "*.*")])

text_out = ScrolledText(master=root)
text_out.grid()
# text_out.insert("0.0", " 00" * 16)
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
            # only open first 4 KiB for now
            content = f.read(1024 * 4)

        _hex = ""

        for byte in content:
            _next_char = ('%x' % byte)
            if len(_next_char) == 1:
                _next_char = "0" + _next_char
            _hex += _next_char + " "

        return _hex
    # just for testing
    return "no file selected"

def save():
    pass

menu.add_command(label="Open", command=_open)
menu.add_command(label="Save", command=save)

root.config(menu=menu)

root.mainloop()