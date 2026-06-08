"""
src/main_window.py

RootWindow configures the main Tk window with title, size, and resize constraints.
Acts as the entry point for the widget hierarchy, initializing and attaching
MFrame as the primary layout container to the root Tk instance.
"""

from tkinter import Tk
from src.views import MFrame


class RootWindow:
    def __init__(self, root: Tk):
        root.title("Window")
        root.geometry("400x400")
        root.resizable(width=False, height=False)
        MFrame(root)

        self.root = root
