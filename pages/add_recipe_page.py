import tkinter as tk
import ttkbootstrap as tkb
from custom import *

# add_recipe_page.py

class AddRecipePage(tk.Frame, Page):
    """
    A class representing the Add Recipe Page.

    This class inherits from tk.Frame and Page classes.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the AddRecipePage object.

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
        # Center the content
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        # Configure column weights to make buttons split equally
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
    
    def _create_ui(self) -> None:
        """
        Create the user interface elements.
        """
        # Header
        self.header = tkb.Label(self, text="Add Recipe Page", font=("Arial", 24), bootstyle=tkb.ACTIVE, anchor="center") # type: ignore
        self.header.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=5)

        # Title
        self.title_label = tk.Label(self, text="Title", font=("Arial", 12))
        self.title_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        self.title_entry = tk.Entry(self)
        self.title_entry.grid(row=1, column=1, columnspan=3, sticky="nsew", padx=10, pady=5)

        # Add button
        self.add_btn = tkb.Button(self, text="Add", bootstyle=tkb.SUCCESS) # type: ignore
        self.add_btn.grid(row=2, column=1, sticky="ew", padx=10, pady=5, ipady=15)
        # Cancel button
        self.cancel_btn = tkb.Button(self, text="Cancel", bootstyle=tkb.DANGER) # type: ignore
        self.cancel_btn.grid(row=2, column=2, sticky="ew", padx=10, pady=5, ipady=15)
        
    def _clear_add_page(self) -> None:
        """
        Clear the input fields on the Add Recipe Page.
        """
        # Clear the title entry
        self.title_entry.delete(0, tk.END)
        
    def get_added_recipe(self) -> str:
        """
        Get the added recipe details from the input fields.

        Returns:
            str: The title of the added recipe.
        """
        title = self.title_entry.get()
        self._clear_add_page()
        return title