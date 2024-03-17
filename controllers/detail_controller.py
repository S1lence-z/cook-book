# detail_controller.py
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
        self.__setup_page()
        
    def __setup_page(self) -> None:
        self._bind_buttons()
    
    def _bind_buttons(self) -> None:
        self.frame.back_btn.config(command=self._go_back)
        self.frame.edit_btn.config(command=self._edit_recipe)
        self.frame.show_ingredients_btn.config(command=self._show_ingredients)
        
    def _go_back(self) -> None:
        self.frame.clear_page()
        self.view.pages["recipesPage"].refresh_page(self.model.get_all_recipes())
        self.view.raise_page("recipesPage")
        
    def _edit_recipe(self) -> None:
        recipe_id = self.frame._recipe_to_display.id
        recipe_to_edit = self.model.get_recipe_by_id(recipe_id)
        edit_page = self.view.pages["editRecipe"]
        edit_page.set_recipe_to_edit(recipe_to_edit)
        self.view.raise_page("editRecipe")
        
    def _show_ingredients(self) -> None:
        print("Showing ingredients")