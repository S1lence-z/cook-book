# view_controller.py
import tkinter as tk
from views.custom_window import AppWindow
from views.home_page import HomePage
from views.edit_recipe_page import EditRecipePage

class ViewController:
    def __init__(self) -> None:
        self.window = AppWindow("CookBook", 1280, 720, False)
        self.pages = {}
        # Add pages
        self._add_page("home", HomePage)
        self._add_page("editRecipe", EditRecipePage)
        
    def _add_page(self, name: str, page) -> None:
        """ Add a page to the pages dictionary.

        Args:
            name (str): The ID of the page.
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