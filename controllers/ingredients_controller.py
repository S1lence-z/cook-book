from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *

class IngredientsController(PageController):
    """
    Controller class for managing ingredients page.
    """

    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        """
        Initializes the IngredientsController.

        Args:
            model (DatabaseManager): The database manager.
            view (MainView): The main view.
        """
        self.model = model
        self.view = view
        self.frame = self.view.pages["ingredientsPage"]
        self.__setup_page()
    
    def __setup_page(self):
        """
        Sets up the ingredients page.
        """
        self._bind_buttons()
    
    def _bind_buttons(self) -> None:
        """
        Binds the buttons to their respective functions.
        """
        self.frame.cancel_btn.config(command=self._cancel)
        
    def _cancel(self) -> None:
        """
        Clears the page and refreshes the recipes page.
        """
        self.frame.clear_page()
        self.view.pages["recipesPage"].refresh_page(self.model.get_all_recipes())
        self.view.raise_page("recipesPage")