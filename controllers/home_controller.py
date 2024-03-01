# home_controller.py
import tkinter as tk
from models.database_manager import DatabaseManager
from controllers import *

class HomeController(PageController):
    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.pages["home"]
        self._add_functionality()
        
    def _add_functionality(self):
        self.frame.add_btn.config(command=self.add_recipe)
        self.frame.delete_btn.config(command=self.delete_recipe)
        self.frame.edit_btn.config(command=self.edit_recipe)
    
    def add_recipe(self) -> None:
        self.view.raise_page("addRecipe")
    
    def delete_recipe(self) -> None:
        #! DELETE THE RECIPE FROM THE DB
        print("Recipe Deleted MOREEEEE")
    
    def edit_recipe(self):
        self.view.raise_page("editRecipe")