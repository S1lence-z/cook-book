# addition_controller.py
from models.database_manager import DatabaseManager
from controllers import *

class AdditionController(PageController):
    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.pages["addRecipe"]
        self._add_functionality()
    
    def _add_functionality(self):
        self.frame.save_btn.config(command=self.save_added_recipe)
        self.frame.cancel_btn.config(command=self.cancel)
    
    def save_added_recipe(self):
        #! SAVE THE RECIPE TO THE DB
        print("RECIPE ADDED")
        self.view.raise_page("home")
    
    def cancel(self):
        self.view.raise_page("home")
        return