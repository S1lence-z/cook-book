from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *

class AddIngredientController(PageController):
    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.pages["addIngredient"]
        self._setup_page()
        
    def _setup_page(self):
        self._bind_buttons()
        
    def _bind_buttons(self) -> None:
        self.frame.add_btn.configure(command=self._save_ingredient)
        self.frame.cancel_btn.configure(command=self._cancel)
        
    def _save_ingredient(self) -> None:
        recipe_id, name, quantity, calories = self.frame.get_added_ingredient()
        self.model.add_ingredient(int(recipe_id), name, quantity, calories)
        all_ingredients = self.model.get_ingredients_by_recipe_id(int(recipe_id))
        self.view.pages["ingredientsPage"].refresh_page(all_ingredients)
        self.view.raise_page("ingredientsPage")
    
    def _cancel(self):
        self.view.raise_page("ingredientsPage")