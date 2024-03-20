from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *

class DetailController(PageController):
    """
    Controller class for the detail page.
    
    Args:
        model (DatabaseManager): The database manager object.
        view (MainView): The main view object.
    """
    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.pages["detailRecipe"]
        self._setup_page()
        
    def _setup_page(self) -> None:
        """
        Sets up the detail page by binding the buttons.
        """
        self._bind_buttons()
    
    def _bind_buttons(self) -> None:
        """
        Binds the button commands to their respective functions.
        """
        self.frame.back_btn.configure(command=self._go_back)
        self.frame.edit_btn.configure(command=self._edit_recipe)
        self.frame.show_ingredients_btn.configure(command=self._show_ingredients)
        self.frame.add_ingredient_btn.configure(command=self._add_ingredient)
        
    def _go_back(self) -> None:
        """
        Clears the page, refreshes the recipes page, and raises it to the top.
        """
        self.view.pages["recipesPage"].refresh_page(self.model.get_all_recipes())
        self.view.raise_page("recipesPage")
        
    def _edit_recipe(self) -> None:
        """
        Retrieves the recipe to edit, sets it in the edit page, and raises the edit page to the top.
        """
        recipe_id = self.frame._recipe_to_display.id
        recipe_to_edit = self.model.get_recipe_by_id(recipe_id)
        self.view.pages["editRecipe"].refresh_page(recipe_to_edit)
        self.view.raise_page("editRecipe")
        
    def _show_ingredients(self) -> None:
        """
        Retrieves the current recipe's ingredients, sets them in the ingredients page, and raises the ingredients page to the top.
        """
        current_recipe_id = self.frame._recipe_to_display.id
        recipe_ingredients = self.model.get_ingredients_by_recipe_id(current_recipe_id)
        self.view.pages["ingredientsPage"].refresh_page(recipe_ingredients, self.frame.get_recipe())
        self.view.raise_page("ingredientsPage")
        
    def _add_ingredient(self) -> None:
        """
        Sets the current recipe in the add ingredient page and raises the add ingredient page to the top.
        """
        self.view.pages["addIngredient"].refresh_page(self.frame.get_recipe())
        self.view.raise_page("addIngredient")