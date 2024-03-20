from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *

class EditationController(PageController):
    """
    Controller class for the editation page.
    """

    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        """
        Initializes the EditationController.

        Args:
            model (DatabaseManager): The database manager.
            view (MainView): The main view.
        """
        self.model = model
        self.view = view
        self.frame = self.view.pages["editRecipe"]
        self._setup_page()

    def _setup_page(self):
        """
        Sets up the editation page.
        """
        self._bind_buttons()

    def _bind_buttons(self) -> None:
        """
        Binds the buttons to their respective functions.
        """
        self.frame.save_btn.configure(command=self._save_edited_recipe)
        self.frame.cancel_btn.configure(command=self._cancel)

    def _save_edited_recipe(self):
        """
        Saves the edited recipe.
        """
        edited_recipe = self.frame.get_edited_recipe()
        self.model.update_recipe(edited_recipe[0], edited_recipe[1], edited_recipe[2], edited_recipe[3], edited_recipe[4], edited_recipe[5], edited_recipe[6])
        self.view.pages["recipesPage"].refresh_page(self.model.get_all_recipes())
        self.view.raise_page("recipesPage")

    def _cancel(self):
        """
        Cancels the editation and returns to the recipes page.
        """
        self.view.pages["recipesPage"].refresh_page(self.model.get_all_recipes())
        self.view.raise_page("recipesPage")