"""
src/main_window.py

RootWindow configures the main Tk window with title, size, and resize constraints.
Acts as the entry point for the widget hierarchy, initializing and attaching
MFrame as the primary layout container to the root Tk instance.
"""

from dataclasses import dataclass
from tkinter import Tk
from src.views import MainFrame
from views.widgets import CellButton


@dataclass(frozen=True)  # makes it immutable
class WindowsConfig:
    title: str = "Window"
    width: int = 300
    height: int = 300
    resizable_w: bool = False
    resizable_h: bool = False


class RootWindow(Tk):
    def __init__(self, config: WindowsConfig = WindowsConfig()):
        super().__init__()
        self.cnf = config

        self._configure()
        self._build()

    def _configure(self):
        self.title(self.cnf.title)
        self.geometry(f"{self.cnf.width}x{self.cnf.height}")
        self.resizable(self.cnf.resizable_w, self.cnf.resizable_h)

    def _build(self):
        MainFrame(self)
        CellButton(self)
