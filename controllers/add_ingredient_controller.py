from audioop import add
from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *
from custom.warning_box import CustomWarningBox

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
        name, quantity, calories = self.frame.get_added_ingredient()
        if not calories.isdigit():
            warning = CustomWarningBox(self.frame, "Invalid Input", "Please enter a valid number for calories.", "300", "200")
            warning.show()
            return
        added_ingredient_recipe_id = self.frame.get_recipe_id()
        self.model.add_ingredient(added_ingredient_recipe_id, name, quantity, calories)
        self.view.pages["ingredientsPage"].refresh_page(self.model.get_ingredients_by_recipe_id(added_ingredient_recipe_id), self.frame.get_recipe())
        self.view.raise_page("ingredientsPage")
    
    def _cancel(self):
        added_ingredient_recipe_id = self.frame.get_recipe_id()
        self.view.pages["ingredientsPage"].refresh_page(self.model.get_ingredients_by_recipe_id(added_ingredient_recipe_id), self.frame.get_recipe())
        self.view.raise_page("ingredientsPage")