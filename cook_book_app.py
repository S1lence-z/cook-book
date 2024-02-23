import tkinter as tk
from views.custom_window import AppWindow
from views.home_page import HomePage
from model.recipe_manager import RecipeManager

class CookBookApp:
    def __init__(self, window: AppWindow, model: RecipeManager) -> None:
        self.window = window
        self.model = model
        self.home_page = HomePage(self.window)