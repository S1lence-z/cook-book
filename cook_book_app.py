# cook_book_app.py
import tkinter as tk
from models.database_manager import DatabaseManager
from controllers.main_controller import MainController
from views.main_view import MainView

class CookBookApp:
    def __init__(self, model: DatabaseManager) -> None:
        """ Initializes the CookBookApp class.

        Args:
            window (AppWindow): Instance of the tk.Tk
            model (DatabaseManager): Instance of the DatabaseManager model class
        """
        self.model = model
        self.view_controller = MainView()
        self.main_controller = MainController(self.model, self.view_controller)