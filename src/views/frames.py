"""
src/frames.py

MFrame is a base frame component that serves as the main layout container.
Subclasses ttk.Frame to integrate directly with Tkinter's widget hierarchy,
allowing it to be used as a self-managing widget within the root Tk window.
"""

from tkinter import ttk


class MFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.grid()
