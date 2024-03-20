# addition_controller.py
from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *

class AdditionController(PageController):
    """
    Controller class for the addition page.
    """

    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        """
        Initializes an instance of the AdditionController class.

        Args:
            model (DatabaseManager): The database manager.
            view (MainView): The main view.
        """
        self.model = model
        self.view = view
        self.frame = self.view.pages["addRecipe"]
        self._setup_page()

    def _setup_page(self):
        """
        Sets up the addition page.
        """
        self._bind_buttons()

    def _bind_buttons(self) -> None:
        """
        Binds the buttons to their respective functions.
        """
        self.frame.add_btn.configure(command=self._edit_added_recipe)
        self.frame.cancel_btn.configure(command=self._cancel)

    def _edit_added_recipe(self):
        """
        Edits the added recipe.
        """
        added_recipe_title = self.frame.get_added_recipe()
        self.model.add_recipe(added_recipe_title)
        added_recipe_id = self.model.get_last_inserted_recipe_id()
        recipe_to_edit = self.model.get_recipe_by_id(added_recipe_id)
        self.view.pages["editRecipe"].refresh_page(recipe_to_edit)
        self.view.raise_page("editRecipe")

    def _cancel(self):
        """
        Cancels the addition and goes back to the recipes page.
        """
        self.view.pages["recipesPage"].refresh_page(self.model.get_all_recipes())
        self.view.raise_page("recipesPage")