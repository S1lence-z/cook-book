# add_recipe_page.py
import tkinter as tk
from views.page_abstract_class import Page

class AddRecipePage(tk.Frame, Page):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._create_ui()
    
    def _create_ui(self) -> None:
        self.header = tk.Label(self, text="Add Recipe Page")
        self.header.pack()
        self.save_button = tk.Button(self, text="moreeee")
        self.save_button.pack()