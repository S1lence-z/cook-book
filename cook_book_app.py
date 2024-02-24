# cook_book_app.py
import tkinter as tk
from model.recipe_manager import RecipeManager
from views.custom_window import AppWindow
from views.home_page import HomePage
from views.add_recipe_page import AddRecipePage
from controllers.home_controller import HomeController
from controllers.addition_controller import AdditionController
from controllers.deletion_controller import DeletionController

class CookBookApp:
    def __init__(self, window: AppWindow, model: RecipeManager) -> None:
        """ Initializes the CookBookApp class.

        Args:
            window (AppWindow): Instance of the tk.Tk class.
            model (RecipeManager): Instance of the RecipeManager model class.
        """
        self.model = model
        self.container = self.create_app_container(window)
        self.init_all_controllers()
        self.init_all_pages(self.container)
        self.raise_page("HomePage")
        
    def create_app_container(self, window: AppWindow) -> tk.Frame:
        """ Creates a super parent frame where all the pages are gonna be displayed.

        Args:
            window (AppWindow): Main application tk.TK window.

        Returns:
            tk.Frame: A frame container for the whole app.
        """
        container = tk.Frame(window)
        container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        return container
    
    def init_all_controllers(self) -> None:
        """ Initializes all the controllers of the app and stores them as key-value pairs. """
        home_controller = HomeController()
        addition_controller = AdditionController()
        deletion_controller = DeletionController()
        self.all_controllers = {
            "HomeController": home_controller,
            "AdditionController": addition_controller,
            "DeletionController": deletion_controller
        }
    
    def init_all_pages(self, whole_app_frame: tk.Frame) -> None:
        """ Initializes all the pages of the app and stores them as key-value pairs. """
        # All the pages 
        home_page = HomePage(whole_app_frame, self.all_controllers["HomeController"])
        add_recipe_page = AddRecipePage(whole_app_frame, self.all_controllers["AdditionController"])
        # Dictionary to store all the pages as key-value pairs
        self.all_pages: dict[str, tk.Frame] = {
            "HomePage": home_page,
            "AddRecipePage": add_recipe_page
        }
        # Show all the pages on tom of each other
        for page in self.all_pages.values():
            page.grid(row=0, column=0, sticky="nsew")
        
    def raise_page(self, page_name: str) -> None:
        """ Takes the page name as an argument and shows the page in the window while hiding all others.

        Args:
            page_name (str): Name of the page from the all_pages dictionary keys.
        """
        page_object = self.all_pages[page_name]
        page_object.tkraise()