from tkinter import ttk


class MFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid()
