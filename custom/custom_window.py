import customtkinter as tkc

class AppWindow(tkc.CTk):
    """AppWindow is a customizable Tkinter window.

    Args:
        title (str): The title of the window.
        width (int): The width of the window.
        height (int): The height of the window.
        resizable (bool): Flag to enable or disable resizability.
        theme (str): The theme for the window.

    Attributes:
        width (int): The width of the window.
        height (int): The height of the window.
    """

    def __init__(self, title: str, width: int, height: int, resizable: bool, theme: str) -> None:
        """Initializes the AppWindow class with the given parameters.

        Args:
            title (str): The title of the window.
            width (int): The width of the window.
            height (int): The height of the window.
            resizable (bool): Flag to enable or disable resizability.
            theme (str): The theme for the window.
        """
        super().__init__()
        self.width = width
        self.height = height
        self.create_title(title)
        self.set_window(width, height, resizable)
        tkc.set_default_color_theme(theme) if theme else print("No theme specified.")
        tkc.set_appearance_mode("system")
        
    def set_window(self, width: int, height: int, resizable: bool) -> None:
        """Sets the window size and resizability settings.

        Args:
            width (int): The width of the window.
            height (int): The height of the window.
            resizable (bool): True if the window is resizable; False otherwise.
        """
        self.geometry(f"{width}x{height}")
        self.resizable(resizable, resizable)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
    def create_title(self, name: str) -> None:
        """Sets the window title.

        Args:
            name (str): The title of the window.
        """
        self.title(name)