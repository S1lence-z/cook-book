# add_recipe_page.py
import tkinter as tk
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
        self._create_ui()
    
    def _create_ui(self) -> None:
        """
        Create the user interface for the Add Recipe Page.
        """
        self.header = tk.Label(self, text="Add Recipe Page")
        # Title
        self.title_label = tk.Label(self, text="Title")
        self.title_label.pack()
        self.title_entry = tk.Entry(self)
        self.title_entry.pack()
        # Description
        self.description_label = tk.Label(self, text="Description")
        self.description_label.pack()
        self.description_text = tk.Text(self, height=10)
        self.description_text.pack()
        # Prep Time
        self.prep_time_label = tk.Label(self, text="Prep Time (minutes)")
        self.prep_time_label.pack()
        self.prep_time_entry = tk.Entry(self)
        self.prep_time_entry.pack()
        # Cook Time
        self.cook_time_label = tk.Label(self, text="Cook Time (minutes)")
        self.cook_time_label.pack()
        self.cook_time_entry = tk.Entry(self)
        self.cook_time_entry.pack()
        # Instructions
        self.instructions_label = tk.Label(self, text="Instructions")
        self.instructions_label.pack()
        self.instructions_text = tk.Text(self, height=10)
        self.instructions_text.pack()
        # Buttons
        self.save_btn = tk.Button(self, text="Save")
        self.save_btn.pack()
        self.cancel_btn = tk.Button(self, text="Cancel")
        self.cancel_btn.pack()
        
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