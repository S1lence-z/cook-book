# home_controller.py
import tkinter as tk
from models.database_manager import DatabaseManager
from controllers.view_controller import ViewController
from views.home_page import HomePage

class HomeController:
    def __init__(self, model: DatabaseManager, view: ViewController) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.pages["home"]
        self._add_functionality()
        
    def _add_functionality(self):
        self.frame.add_button.config(command=self.add_recipe)
    
    def add_recipe(self) -> None:
        self.view.raise_page("editRecipe")
        pass
    
    def delete_recipe(self) -> None:
        print("delete more")
        pass