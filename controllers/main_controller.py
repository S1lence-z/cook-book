# main_controller.py
from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *

class MainController:
    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        """
        Initialize the MainController.

        Args:
            model (DatabaseManager): The database manager.
            view (MainView): The main view.
        """
        self.database_manager = model
        self.view = view
        self.page_controllers = self._init_page_controllers()
    
    def _init_page_controllers(self) -> list[PageController]:
        """ Initialize all controllers.

        Returns:
            list: A list of all controllers.
        """
        recipes_controller = RecipesController(self.database_manager, self.view)
        editation_controller = EditationController(self.database_manager, self.view)
        addition_controller = AdditionController(self.database_manager, self.view)
        detail_controller = DetailController(self.database_manager, self.view)
        ingredients_controller = IngredientsController(self.database_manager, self.view)
        return [recipes_controller, editation_controller, addition_controller, detail_controller, ingredients_controller]
    
    def start_mainloop(self):
        """
        Start the main loop of the application.
        """
        self.view.raise_page("recipesPage")
        self.view.start_mainloop()