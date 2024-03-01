# editation_controller.py
from models.database_manager import DatabaseManager
from controllers import *

class EditationController(PageController):
    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.pages["editRecipe"]
        self._setup_page()
        
    def _setup_page(self):
        self._bind_buttons()
        
    def _bind_buttons(self) -> None:
        self.frame.save_btn.config(command=self.save_edited_recipe)
        self.frame.cancel_btn.config(command=self.cancel)
    
    def save_edited_recipe(self):
        #! SAVE THE RECIPE TO THE DB
        print("RECIPE EDITED")
        self.view.raise_page("home")
    
    def cancel(self):
        self.view.raise_page("home")