# main_controller.py
from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *

class MainController:
    def __init__(self, models: list, view: MainView) -> None:
        self.database_manager = models[0]
        self.ingredients_manager = models[1]
        self.view = view
        self.page_controllers = self._init_page_controllers()
    
    def _init_page_controllers(self) -> list[PageController]:
        """ Initialize all controllers.

        Returns:
            list: A list of all controllers.
        """
        home_controller = RecipesController(self.database_manager, self.view)
        editation_controller = EditationController(self.database_manager, self.view)
        addition_controller = AdditionController(self.database_manager, self.view)
        detail_controller = DetailController(self.database_manager, self.view)
        ingredients_controller = IngredientsController(self.ingredients_manager, self.view)
        return [home_controller, editation_controller, addition_controller, detail_controller, ingredients_controller]
    
    def start_mainloop(self):
        self.view.raise_page("recipesPage")
        self.view.start_mainloop()