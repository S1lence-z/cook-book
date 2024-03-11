# detail_recipe_page.py
import tkinter as tk
from custom import *

class DetailRecipePage(tk.Frame, Page):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._recipe_to_display: Recipe
        self._create_ui()
        
    def _create_ui(self) -> None:
        self.header = tk.Label(self, text="Recipe Detail Page")
        self.header.pack()
        # Title
        self.title_label = tk.Label(self, text="Title")
        self.title_label.pack()
        self.title_value = tk.Label(self, text=self._recipe_to_display.title)
        self.title_value.pack()
        # Description
        self.description_label = tk.Label(self, text="Description")
        self.description_label.pack()
        self.description_value = tk.Label(self, text=self._recipe_to_display.description, wraplength=500)
        self.description_value.pack()
        # Prep Time
        self.prep_time_label = tk.Label(self, text="Prep Time (minutes)")
        self.prep_time_label.pack()
        self.prep_time_value = tk.Label(self, text=self._recipe_to_display.prep_time)
        self.prep_time_value.pack()
        # Cook Time
        self.cook_time_label = tk.Label(self, text="Cook Time (minutes)")
        self.cook_time_label.pack()
        self.cook_time_value = tk.Label(self, text=self._recipe_to_display.cook_time)
        self.cook_time_value.pack()
        # Instructions
        self.instructions_label = tk.Label(self, text="Instructions")
        self.instructions_label.pack()
        self.instructions_value = tk.Label(self, text=self._recipe_to_display.instructions, wraplength=500)
        self.instructions_value.pack()
        
    def set_recipe_to_display(self, recipe: Recipe):
        self._recipe_to_display = recipe
        self._fill_the_display_page()
        
    def _clear_display_page(self):
        pass
        
    def _fill_the_display_page(self):
        pass