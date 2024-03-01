# view_controller.py
import tkinter as tk
from views.custom_window import AppWindow
from pages import *

class MainView:
    def __init__(self) -> None:
        self.window = self._create_app_window("CookBook", 1280, 720, False)
        self.pages = {}
        # Add pages
        self._add_page("home", HomePage)
        self._add_page("editRecipe", EditRecipePage)
        self._add_page("addRecipe", AddRecipePage)
        
    def _create_app_window(self, title: str, width: int, height: int, resizability: bool):
        return AppWindow(title, width, height, resizability)
        
    def _add_page(self, name: str, page) -> None:
        """ Add a page to the pages dictionary.

        Args:
            name (str): The name of the page.
            page (str): The name of the class of the page.
        """
        self.pages[name] = page(self.window)
        self.pages[name].grid(row=0, column=0, sticky="nsew")
    
    def raise_page(self, page_name: str) -> None:
        """ Takes the page name as an argument and shows the page in the window while hiding all others.

        Args:
            page_name (str): Name of the page from the all_pages dictionary keys.
        """
        page = self.pages[page_name]
        page.tkraise()
    
    def start_mainloop(self):
        """ Start the mainloop of the Tkinter window. """
        self.window.mainloop()