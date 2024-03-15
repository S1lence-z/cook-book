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
        
    def _go_back(self) -> None:
        self.view.raise_page("home")