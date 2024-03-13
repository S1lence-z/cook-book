# add_recipe_page.py
import tkinter as tk
import ttkbootstrap as tkb
from custom import *

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
        # Center the content
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # Configure column weights to make buttons split equally
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
    
    def _create_ui(self) -> None:
        self.header = tkb.Label(self, text="Add Recipe Page", font=("Arial", 24), bootstyle=tkb.ACTIVE, anchor="center") # type: ignore
        self.header.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=5)

        # Title
        self.title_label = tk.Label(self, text="Title", font=("Arial", 12))
        self.title_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        self.title_entry = tk.Entry(self)
        self.title_entry.grid(row=1, column=1, columnspan=3, sticky="nsew", padx=10, pady=5)

        # Description
        self.description_label = tk.Label(self, text="Description", font=("Arial", 12))
        self.description_label.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        self.description_text = tk.Text(self, height=10)
        self.description_text.grid(row=2, column=1, columnspan=3, sticky="nsew", padx=10, pady=5)

        # Prep Time
        self.prep_time_label = tk.Label(self, text="Prep Time (minutes)", font=("Arial", 12))
        self.prep_time_label.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)
        self.prep_time_entry = tk.Entry(self)
        self.prep_time_entry.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

        # Cook Time
        self.cook_time_label = tk.Label(self, text="Cook Time (minutes)", font=("Arial", 12))
        self.cook_time_label.grid(row=3, column=2, sticky="nsew", padx=10, pady=5)
        self.cook_time_entry = tk.Entry(self)
        self.cook_time_entry.grid(row=3, column=3, sticky="nsew", padx=10, pady=5)

        # Instructions
        self.instructions_label = tk.Label(self, text="Instructions", font=("Arial", 12))
        self.instructions_label.grid(row=5, column=0, sticky="nsew", padx=10, pady=5)
        self.instructions_text = tk.Text(self, height=10)
        self.instructions_text.grid(row=5, column=1, columnspan=3, sticky="nsew", padx=10, pady=5)

        # Add button
        self.save_btn = tkb.Button(self, text="Add", bootstyle=tkb.SUCCESS) # type: ignore
        self.save_btn.grid(row=6, column=1, columnspan=2, sticky="nsew", padx=10, pady=5, ipady=15)
        # Cancel button
        self.cancel_btn = tkb.Button(self, text="Cancel", bootstyle=tkb.DANGER) # type: ignore
        self.cancel_btn.grid(row=6, column=3, sticky="nsew", padx=10, pady=5, ipady=15)
        
    def _clear_add_page(self):
        """
        Clear the input fields on the Add Recipe Page.
        """
        # Clear the title entry
        self.title_entry.delete(0, tk.END)
        # Clear the description text.
        self.description_text.delete('1.0', tk.END)
        # Clear the prep time entry
        self.prep_time_entry.delete(0, tk.END)
        # Clear the cook time entry
        self.cook_time_entry.delete(0, tk.END)
        # Clear the instructions text.
        self.instructions_text.delete('1.0', tk.END)
        
    def get_added_recipe(self) -> list:
        """
        Get the added recipe details from the input fields.

        Returns:
            list: A list containing the title, description, prep time, cook time, and instructions.
        """
        title = self.title_entry.get()
        description = self.description_text.get("1.0", "end-1c")
        prep_time = self.prep_time_entry.get()
        cook_time = self.cook_time_entry.get()
        instructions = self.instructions_text.get("1.0", "end-1c")
        self._clear_add_page()
        return [title, description, prep_time, cook_time, instructions]