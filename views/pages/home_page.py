# home_page.py
from ast import Delete
import tkinter as tk
from views.page_abc import Page

class HomePage(tk.Frame, Page):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._create_ui()
        
    def _create_ui(self):
        self.header = tk.Label(self, text="Home Page")
        self.header.pack()
        self.add_btn = tk.Button(self, text="Add Recipe")
        self.add_btn.pack()
        self.delete_btn = tk.Button(self, text="Delete Recipe")
        self.delete_btn.pack()
        self.edit_btn = tk.Button(self, text="Edit Recipe")
        self.edit_btn.pack()