from models.ingredients_manager import IngredientsManager
from views.main_view import MainView
from controllers import *

class IngredientsController(PageController):
    def __init__(self, model: IngredientsManager, view: MainView) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.pages["ingredientsPage"]
        self.__setup_page()
    
    def __setup_page(self):
        self._bind_buttons()
    
    def _bind_buttons(self) -> None:
        self.frame.cancel_btn.config(command=self._cancel)
        
    def _cancel(self) -> None:
        print("Cancel button clicked")