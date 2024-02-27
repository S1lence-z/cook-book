# home_page.py
import tkinter as tk
from .page_abstract_class import Page

class HomePage(tk.Frame, Page):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.create_ui()
        
    def create_ui(self):
        self.header = tk.Label(self, text="All Recipes")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.add_button = tk.Button(self, text="Add Recipe")
        self.add_button.grid(row=3, column=1, padx=0, pady=10, sticky="w")