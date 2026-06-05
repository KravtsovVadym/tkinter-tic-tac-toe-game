from src.main_window import RootWindow

from tkinter import Tk


def tk_app():
    root = Tk()  # - The main application window
    RootWindow(root)
    root.mainloop()


if __name__ == "__main__":
    tk_app()
