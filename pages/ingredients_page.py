import tkinter as tk
import ttkbootstrap as tkb
from custom import *

class IngredientsPage(tk.Frame, Page):
    """
    A class representing the Ingredients Page.

    This class inherits from tk.Frame and Page classes.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the IngredientsPage object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._ingredients_to_display: list[Ingredient]
        self._format_frame()
        self._create_ui()
        
    def _format_frame(self) -> None:
        """
        Format the frame layout.
        """
        for i in range(2):
            self.grid_columnconfigure(i, weight=1)
        for i in range(4):
            self.grid_rowconfigure(i, weight=1)
    
    def _create_ui(self) -> None:
        """
        Create the user interface elements.
        """
        # Header
        self.header = tkb.Label(self, text="Ingredients Page", font=("Arial", 24), bootstyle=tkb.ACTIVE, anchor="center") # type: ignore
        self.header.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)
        # Ingredients List
        self.ingredients_list_label = tkb.Label(self, text="Ingredients of", font=("Arial", 16), bootstyle=tkb.ACTIVE, anchor="center") # type: ignore
        self.ingredients_list_label.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)
        self.ingredients_list = IngredientsList(self, font=("Arial", 12))
        self.ingredients_list.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)
        # Generate PDF button
        self.generate_pdf_btn = tkb.Button(self, text="Generate PDF", bootstyle=tkb.SUCCESS) # type: ignore
        self.generate_pdf_btn.grid(row=3, column=0, sticky="ew", padx=10, pady=5, ipady=15)
        # Cancel button
        self.cancel_btn = tkb.Button(self, text="Cancel", bootstyle=tkb.DANGER) # type: ignore
        self.cancel_btn.grid(row=3, column=1, sticky="ew", padx=10, pady=5, ipady=15)
        
    def set_ingredients_to_display(self, ingredients: list[Ingredient], recipe_name: str) -> None:
        """
        Set the ingredients to display.

        Args:
            ingredients (list[Ingredient]): The ingredients to display.
        """
        self._ingredients_to_display = ingredients
        self._fill_the_ingredients_page(recipe_name)
        
    def clear_page(self) -> None:
        """
        Clear the page.
        """
        self.ingredients_list.clear()
        
    def _fill_the_ingredients_page(self, recipe_name: str) -> None:
        """
        Fill the ingredients page with the given recipe.

        Args:
            recipe (Recipe): The recipe to fill the page with.
        """
        self.ingredients_list_label.config(text=f"Ingredients of {recipe_name}")
        self.ingredients_list.populate(self._ingredients_to_display)