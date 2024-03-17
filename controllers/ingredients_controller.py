from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *

class IngredientsController(PageController):
    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.pages["ingredientsPage"]
        self.__setup_page()
    
    def __setup_page(self):
        self._bind_buttons()
    
    def _bind_buttons(self) -> None:
        self.frame.cancel_btn.config(command=self._cancel)
        
    def _cancel(self) -> None:
        self.frame.clear_page()
        self.view.pages["recipesPage"].refresh_page(self.model.get_all_recipes())
        self.view.raise_page("recipesPage")