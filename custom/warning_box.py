import tkinter as tk

class CustomWarningBox:
    """
    A custom warning box class for displaying warning messages.

    Args:
        root (tk.Tk): The root Tkinter window.
        title (str): The title of the warning box.
        message (str): The message to be displayed in the warning box.
        width (str): The width of the warning box.
        height (str): The height of the warning box.
    """

    def __init__(self, root: tk.Tk, title: str, message: str, width: str, height: str) -> None:
        """
        Initializes a new instance of the CustomWarningBox class.

        Args:
            root (tk.Tk): The root Tkinter window.
            title (str): The title of the warning box.
            message (str): The message to be displayed in the warning box.
            width (str): The width of the warning box.
            height (str): The height of the warning box.
        """
        self.root = root
        self.title = title
        self.message = message
        self.width = width
        self.height = height

    def show(self) -> None:
        """
        Displays the warning box.
        """
        self.window = tk.Toplevel(self.root)
        self.window.title(self.title)
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.resizable(False, False)

        self.label = tk.Label(self.window, text=self.message, font=("Arial", 12))
        self.label.pack(pady=20)

        self.button = tk.Button(self.window, text="Ok", command=self.window.destroy)
        self.button.pack(pady=10)
        
    def set_title(self, title: str) -> None:
        """
        Sets the title of the warning box.

        Args:
            title (str): The new title of the warning box.
        """
        self.title = title
        
    def set_message(self, message: str) -> None:
        """
        Sets the message to be displayed in the warning box.

        Args:
            message (str): The new message to be displayed in the warning box.
        """
        self.message = message