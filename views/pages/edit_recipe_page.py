# edit_recipe_page.py
import tkinter as tk
from views.page_abc import Page

class EditRecipePage(tk.Frame, Page):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._create_ui()
    
    def _create_ui(self):
        self.header = tk.Label(self, text="Edit Recipe Page")
        self.header.pack()
        self.save_btn = tk.Button(self, text="Save and go Home")
        self.save_btn.pack()
        self.cancel_btn = tk.Button(self, text="Cancel")
        self.cancel_btn.pack()