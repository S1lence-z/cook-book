# editation_controller.py
from models.database_manager import DatabaseManager
from controllers.view_controller import ViewController
from controllers.page_controller_abc import PageController

class EditationController(PageController):
    def __init__(self, model: DatabaseManager, view: ViewController) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.pages["editRecipe"]
        self._add_functionality()
        
    def _add_functionality(self):
        self.frame.save_btn.config(command=self.save_edited_recipe)
        self.frame.cancel_btn.config(command=self.cancel)
    
    def save_edited_recipe(self):
        #! SAVE THE RECIPE TO THE DB
        print("RECIPE EDITED")
        self.view.raise_page("home")
    
    def cancel(self):
        self.view.raise_page("home")
        return