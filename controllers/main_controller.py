# main_controller.py
from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *

class MainController:
    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        self.model = model
        self.view = view
        self.page_controllers = self._init_page_controllers()
    
    def _init_page_controllers(self) -> list[PageController]:
        """ Initialize all controllers.

        Returns:
            list: A list of all controllers.
        """
        home_controller = HomeController(self.model, self.view)
        editation_controller = EditationController(self.model, self.view)
        addition_controller = AdditionController(self.model, self.view)
        detail_controller = DetailController(self.model, self.view)
        return [home_controller, editation_controller, addition_controller, detail_controller]
    
    def start_mainloop(self):
        self.view.raise_page("home")
        self.view.start_mainloop()