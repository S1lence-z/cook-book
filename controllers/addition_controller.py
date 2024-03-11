# addition_controller.py
from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *

class AdditionController(PageController):
    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.pages["addRecipe"]
        self.__setup_page()
    
    def __setup_page(self):
        self._bind_buttons()
        
    def _bind_buttons(self) -> None:
        self.frame.save_btn.config(command=self.save_added_recipe)
        self.frame.cancel_btn.config(command=self.cancel)
    
    def save_added_recipe(self):
        added_recipe = self.frame.get_added_recipe()
        self.model.add_recipe(added_recipe[0], added_recipe[1], added_recipe[2], added_recipe[3], added_recipe[4])
        new_model = self.model.get_all_recipes()
        self.view.raise_page("home")
        self.view.pages["home"].update_recipe_list(new_model)
    
    def cancel(self):
        self.view.raise_page("home")
        return