from tkinter import ttk


class RootWindow:
    def __init__(self, root: ttk):
        self.frm = ttk.Frame(root)
        self.frm.grid()
