# custom_window.py
import tkinter as tk

class AppWindow(tk.Tk):
    """ AppWindow is a customizable Tkinter window. """
    def __init__(self, title: str, width: int, height: int, resizable: bool) -> None:
        """Initializes the AppWindow class with given params.

        Args:
            title (str): Sets the window title.
            width (int): Sets the Tkinter window width.
            height (int): Sets the Tkinter window height.
            resizable (bool): Flag to enable or disable resizability.
        """
        super().__init__()
        # Methods to initilize the window
        self.create_title(title)
        self.window_settings(width, height, resizable)
        
    def window_settings(self, width: int, height: int, resizable: bool) -> None:
        """Sets the window size and resizability settings.

        Args:
            width (int): Width of the window.
            height (int): Height of the window.
            resizable (bool): True if the window is resizable; else False.
        """
        self.geometry(f"{width}x{height}")
        self.resizable(resizable, resizable)
        
    def create_title(self, name: str) -> None:
        """Sets the window title.

        Args:
            name (str): The title of the window.
        """
        self.title(name)