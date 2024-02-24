# add_recipe_page.py
import tkinter as tk
from .custom_window import AppWindow


class AddRecipePage:
    def __init__(self, window: AppWindow) -> None:
        self.window = window
        self.create_ui()
        
    def create_ui(self):
        return