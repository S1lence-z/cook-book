# edit_recipe_page.py
import tkinter as tk
from custom.page_abc import Page
from models.recipe import Recipe

class EditRecipePage(tk.Frame, Page):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._recipe_to_edit = None
        self._create_ui()
    
    def _create_ui(self) -> None:
        self.header = tk.Label(self, text="Edit Recipe Page")
        self.header.pack()
        # ALL RECIPE ATTRIBUTES
        
        # ALL BUTTONS
        self.save_btn = tk.Button(self, text="Save and go Home")
        self.save_btn.pack()
        self.cancel_btn = tk.Button(self, text="Cancel")
        self.cancel_btn.pack()
        
    def set_recipe_to_edit(self, recipe: Recipe):
        self._recipe_to_edit = recipe