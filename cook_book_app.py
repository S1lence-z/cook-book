# cook_book_app.py
from models.database_manager import DatabaseManager
from controllers.main_controller import MainController
from views.main_view import MainView
from custom import AppWindow

class CookBookApp:
    def __init__(self, model: DatabaseManager) -> None:
        """ Initializes the CookBookApp class.

        Args:
            model (DatabaseManager): Instance of the DatabaseManager model class
        """
        self._model = model
        self._app_window = self._create_app_window("CookBook", 1280, 720, True, "green")
        self._view_controller = MainView(self._app_window)
        self._main_controller = MainController(self._model, self._view_controller)
        
    def start_app(self):
        """ Starts the application. """
        self._main_controller.start_mainloop()
        
    def _create_app_window(self, title: str, width: int, height: int, resizability: bool, theme: str) -> AppWindow:
        """
        Creates an application window.

        Args:
            title (str): The title of the window.
            width (int): The width of the window.
            height (int): The height of the window.
            resizability (bool): Whether the window can be resized or not.
            theme (str): The theme of the window.

        Returns:
            AppWindow: The created application window.
        """
        return AppWindow(title, width, height, resizability, theme)