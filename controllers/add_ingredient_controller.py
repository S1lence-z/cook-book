from audioop import add
from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *
from custom.warning_box import CustomWarningBox

class AddIngredientController(PageController):
    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        """
        Initializes the AddIngredientController.

        Args:
            model (DatabaseManager): The database manager.
            view (MainView): The main view.
        """
        self.model = model
        self.view = view
        self.frame = self.view.pages["addIngredient"]
        self._setup_page()
        
    def _setup_page(self):
        """
        Sets up the page.
        """
        self._bind_buttons()
        
    def _bind_buttons(self) -> None:
        """
        Binds the buttons to their respective functions.
        """
        self.frame.add_btn.configure(command=self._save_ingredient)
        self.frame.cancel_btn.configure(command=self._cancel)
        
    def _save_ingredient(self) -> None:
        """
        Saves the ingredient to the database.
        """
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
        """
        Cancels the addition of the ingredient and returns to the ingredients page.
        """
        added_ingredient_recipe_id = self.frame.get_recipe_id()
        self.view.pages["ingredientsPage"].refresh_page(self.model.get_ingredients_by_recipe_id(added_ingredient_recipe_id), self.frame.get_recipe())
        self.view.raise_page("ingredientsPage")