from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *
from pdf_converter.pdf_generator import PdfGenerator

class IngredientsController(PageController):
    """
    Controller class for managing ingredients page.
    """

    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        """
        Initializes the IngredientsController.

        Args:
            model (DatabaseManager): The database manager.
            view (MainView): The main view.
        """
        self.model = model
        self.view = view
        self.frame = self.view.pages["ingredientsPage"]
        self._pdf_generator = PdfGenerator(self.view)
        self._setup_page()
    
    def _setup_page(self):
        """
        Sets up the ingredients page.
        """
        self._bind_buttons()
    
    def _bind_buttons(self) -> None:
        """
        Binds the buttons to their respective functions.
        """
        self.frame.cancel_btn.configure(command=self._go_back)
        self.frame.generate_pdf_btn.configure(command=self._generate_pdf)
        self.frame.add_ingredient_btn.configure(command=self._add_ingredient)
        
    def _go_back(self) -> None:
        """
        Clears the page and refreshes the recipes page.
        """
        self.view.pages["detailRecipe"].refresh_page(self.frame.get_recipe())
        self.view.raise_page("detailRecipe")
        
    def _generate_pdf(self) -> None:
        """
        Generates a PDF file with the ingredients.
        """
        ingredients_list = self.frame.get_ingredients_list()
        recipe_title = self.frame.get_recipe_title()
        self._pdf_generator.generate_pdf(ingredients_list, recipe_title)
        
    def _add_ingredient(self) -> None:
        """
        Adds a new ingredient to the recipe.
        """
        self.view.pages["addIngredient"].refresh_page(self.frame.get_recipe())
        self.view.raise_page("addIngredient")