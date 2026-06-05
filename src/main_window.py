from tkinter import Tk
from src.views import MFrame


class RootWindow:
    def __init__(self, root: Tk):
        root.title("Window")
        root.geometry("400x400")
        root.resizable(width=False, height=False)
        MFrame(root)

        self.root = root
