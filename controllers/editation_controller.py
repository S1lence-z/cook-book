# editation_controller.py
from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *

class EditationController(PageController):
    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.pages["editRecipe"]
        self.__setup_page()
        
    def __setup_page(self):
        self._bind_buttons()
        
    def _bind_buttons(self) -> None:
        self.frame.save_btn.config(command=self._save_edited_recipe)
        self.frame.cancel_btn.config(command=self._cancel)
    
    def _save_edited_recipe(self):
        edited_recipe = self.frame.get_edited_recipe()
        self.model.update_recipe(edited_recipe[0], edited_recipe[1], edited_recipe[2], edited_recipe[3], edited_recipe[4], edited_recipe[5], edited_recipe[6])
        self.view.pages["recipesPage"].refresh_page(self.model.get_all_recipes())
        self.view.raise_page("recipesPage")
    
    def _cancel(self):
        self.view.pages["recipesPage"].refresh_page(self.model.get_all_recipes())
        self.view.raise_page("recipesPage")