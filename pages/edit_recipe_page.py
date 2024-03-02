import tkinter as tk
from custom import *

class EditRecipePage(tk.Frame, Page):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._recipe_to_edit: Recipe
        self._create_ui()

    def _create_ui(self) -> None:
        self.header = tk.Label(self, text="Edit Recipe Page")
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

    def set_recipe_to_edit(self, recipe: Recipe):
        self._recipe_to_edit = recipe
        self._fill_the_edit_page()
        
    def _clear_edit_page(self):
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
            
    def _fill_the_edit_page(self) -> None:
        self._clear_edit_page()
        # Fill the form with the recipe's current values
        self.title_entry.insert(0, self._recipe_to_edit.title)
        self.description_text.insert(tk.END, self._recipe_to_edit.description)
        self.prep_time_entry.insert(0, str(self._recipe_to_edit.prep_time))
        self.cook_time_entry.insert(0, str(self._recipe_to_edit.cook_time))
        self.instructions_text.insert(tk.END, self._recipe_to_edit.instructions)
        
    def get_edited_recipe(self):
        recipe_id = self._recipe_to_edit.id
        title = self.title_entry.get()
        description = self.description_text.get("1.0")
        prep_time = self.prep_time_entry.get()
        cook_time = self.cook_time_entry.get()
        instructions = self.instructions_text.get("1.0")
        return [recipe_id, title, description, prep_time, cook_time, instructions]