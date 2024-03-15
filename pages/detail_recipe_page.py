# detail_recipe_page.py
import tkinter as tk
import ttkbootstrap as tkb
from custom import *

class DetailRecipePage(tk.Frame, Page):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._recipe_to_display: Recipe
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
        
    def _create_ui(self) -> None:
        self.font = ("Arial", 16)
        self.header = tk.Label(self, text="Recipe Detail Page", font=self.font + ("bold",))
        self.header.grid(row=0, column=0, columnspan=2, pady=10)
        # Title
        self.title_label = tk.Label(self, text="Title", font=self.font + ("bold",))
        self.title_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        self.title_value = tk.Label(self, font=self.font)
        self.title_value.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)
        # Description
        self.description_label = tk.Label(self, text="Description", font=self.font + ("bold",))
        self.description_label.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        self.description_value = tk.Label(self, font=self.font)
        self.description_value.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
        # Prep Time
        self.prep_time_label = tk.Label(self, text="Prep Time", font=self.font + ("bold",))
        self.prep_time_label.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)
        self.prep_time_value = tk.Label(self, font=self.font)
        self.prep_time_value.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)
        # Cook Time
        self.cook_time_label = tk.Label(self, text="Cook Time", font=self.font + ("bold",))
        self.cook_time_label.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)
        self.cook_time_value = tk.Label(self, font=self.font)
        self.cook_time_value.grid(row=4, column=1, sticky="nsew", padx=10, pady=5)
        # Instructions
        self.instructions_label = tk.Label(self, text="Instructions", font=self.font + ("bold",))
        self.instructions_label.grid(row=5, column=0, sticky="nsew", padx=10, pady=5)
        self.instructions_value = tk.Label(self, font=self.font)
        self.instructions_value.grid(row=5, column=1, sticky="nsew", padx=10, pady=5)
        # Back button
        self.back_btn = tkb.Button(self, text="Back", bootstyle=tkb.DANGER) # type: ignore
        self.back_btn.grid(row=6, column=0, pady=10, padx=10, sticky="nsew")
        # Show ingredients button
        self.show_ingredients_btn = tkb.Button(self, text="Show Ingredients", bootstyle=tkb.INFO) # type: ignore
        self.show_ingredients_btn.grid(row=6, column=1, pady=10, padx=10, sticky="nsew")
        
    def set_recipe_to_display(self, recipe: Recipe):
        self._recipe_to_display = recipe
        self._fill_the_display_page()
        
    def _fill_the_display_page(self):
        self.title_value.config(text=self._recipe_to_display.title)
        self.description_value.config(text=self._recipe_to_display.description)
        self.prep_time_value.config(text=f"{self._recipe_to_display.prep_time} minutes")
        self.cook_time_value.config(text=f"{self._recipe_to_display.cook_time} minutes")
        self.instructions_value.config(text=self._recipe_to_display.instructions)