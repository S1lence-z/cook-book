# main_controller.py
from models.database_manager import DatabaseManager
from controllers.view_controller import ViewController
from controllers.home_controller import HomeController
from controllers.editation_controller import EditationController

class MainController:
    def __init__(self, model: DatabaseManager, view: ViewController) -> None:
        self.model = model
        self.view = view
        self.page_controllers = self._init_page_controllers()
    
    def start_app(self) -> None:
        """ Start the tk.Tk mainloop (starts the tkinter application) """
        self.view.container.mainloop()
        
    def _init_page_controllers(self) -> list:
        """ Initialize all controllers.

        Returns:
            list: A list of all controllers.
        """
        home_controller = HomeController(self.model, self.view)
        editation_controller = EditationController(self.model, self.view)
        return [home_controller, editation_controller]