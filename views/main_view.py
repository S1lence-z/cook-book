from custom import *
from pages import *

class MainView:
    def __init__(self, window: AppWindow) -> None:
        """
        Initializes the MainView class.

        Args:
            window (AppWindow): The application window.

        Creates an instance of the MainView class, initializes the pages dictionary, and adds pages to it.
        """
        self.window = window
        self.pages = {}
        # Add pages
        self._add_page("recipesPage", RecipesPage)
        self._add_page("editRecipe", EditRecipePage)
        self._add_page("addRecipe", AddRecipePage)
        self._add_page("detailRecipe", DetailRecipePage)
        self._add_page("ingredientsPage", IngredientsPage)
        self._add_page("addIngredient", AddIngredientPage)
        
    def _add_page(self, name: str, page) -> None:
        """ 
        Add a page to the pages dictionary.

        Args:
            name (str): The name of the page.
            page (str): The class of the page.
        """
        self.pages[name] = page(self.window)
        self.pages[name].grid(row=0, column=0, sticky="nsew")
    
    def raise_page(self, page_name: str) -> None:
        """ 
        Raises a specific page in the window while hiding all others.

        Args:
            page_name (str): The name of the page to be raised.
        """
        page = self.pages[page_name]
        page.tkraise()
    
    def start_mainloop(self):
        """ 
        Starts the mainloop of the Tkinter window.
        """
        self.window.mainloop()