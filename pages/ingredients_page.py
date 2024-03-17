import tkinter as tk
import ttkbootstrap as tkb
from custom import *

class IngredientsPage(tk.Frame, Page):
    """
    A class representing the Ingredients Page.

    This class inherits from tk.Frame and Page classes.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the IngredientsPage object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._format_frame()
        self._create_ui()
        
    def _format_frame(self) -> None:
        """
        Format the frame layout.
        """
        for i in range(2):
            self.grid_columnconfigure(i, weight=1)
        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
    
    def _create_ui(self) -> None:
        """
        Create the user interface elements.
        """
        # Header
        self.header = tkb.Label(self, text="Ingredients Page", font=("Arial", 24), bootstyle=tkb.ACTIVE, anchor="center") # type: ignore
        self.header.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=5)
        # Name
        self.name_label = tk.Label(self, text="Name", font=("Arial", 12))
        self.name_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, columnspan=3, sticky="nsew", padx=10, pady=5)
        # Cancel button
        self.cancel_btn = tkb.Button(self, text="Cancel", bootstyle=tkb.DANGER) # type: ignore
        self.cancel_btn.grid(row=2, column=2, sticky="ew", padx=10, pady=5, ipady=15)
        
    def _clear_add_page(self) -> None:
        """
        Clear the input fields on the Ingredients Page.
        """
        pass