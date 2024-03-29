import customtkinter as tkc
from custom import *

class AddIngredientPage(tkc.CTkFrame, Page):
    """
    A class representing the Add Ingredient Page.

    This class inherits from tkc.CTkFrame and Page classes.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the AddIngredientPage object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._recipe: Recipe
        self._format_frame()
        self._create_ui()
        
    def _format_frame(self) -> None:
        """
        Format the frame layout.
        """
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        for i in range(4):
            self.grid_rowconfigure(i, weight=1)
    
    def _create_ui(self) -> None:
        """
        Creates the user interface elements for the 'Add Ingredient Page' with a modern look.
        """
        # Font and color settings
        font_family = "Segoe UI"
        base_font_size = 18
        header_font_size = 28
        font_settings = (font_family, base_font_size)
        header_font_settings = (font_family, header_font_size)

        # Header label
        self.header = tkc.CTkLabel(self, text="Add Ingredient Page", font=header_font_settings)
        self.header.grid(row=0, column=0, columnspan=3, sticky="ew", padx=20, pady=10)

        # Name
        self.name_label = tkc.CTkLabel(self, text="Name", font=font_settings)
        self.name_label.grid(row=1, column=0, sticky="e", padx=20, pady=10)
        self.name_entry = tkc.CTkEntry(self, font=font_settings)
        self.name_entry.grid(row=1, column=1, columnspan=2, sticky="ew", padx=20, pady=10)
        
        # Quantity
        self.quantity_label = tkc.CTkLabel(self, text="Quantity", font=font_settings)
        self.quantity_label.grid(row=2, column=0, sticky="e", padx=20, pady=10)
        self.quantity_entry = tkc.CTkEntry(self, font=font_settings)
        self.quantity_entry.grid(row=2, column=1, columnspan=2, sticky="ew", padx=20, pady=10)
        
        # Calories
        self.calories_label = tkc.CTkLabel(self, text="Calories", font=font_settings)
        self.calories_label.grid(row=3, column=0, sticky="e", padx=20, pady=10)
        self.calories_entry = tkc.CTkEntry(self, font=font_settings)
        self.calories_entry.grid(row=3, column=1, columnspan=2, sticky="ew", padx=20, pady=10)

        # Sidebar frame for action buttons
        self.sidebar_frame = tkc.CTkFrame(self)
        self.sidebar_frame.grid(row=0, column=3, rowspan=4, sticky="nsew", padx=20, pady=10)

        # Save button
        self.add_btn = tkc.CTkButton(self.sidebar_frame, text="Save", font=font_settings, fg_color="green")
        self.add_btn.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        # Cancel button
        self.cancel_btn = tkc.CTkButton(self.sidebar_frame, text="Cancel", font=font_settings, fg_color="red")
        self.cancel_btn.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
    def _set_recipe(self, recipe: Recipe) -> None:
        """
        Set the recipe for the AddIngredientPage.

        Args:
            recipe: The recipe object.
        """
        self._recipe = recipe
        
    def get_recipe(self) -> Recipe:
        """
        Get the recipe object.

        Returns:
            The recipe object.
        """
        return self._recipe
    
    def get_recipe_id(self) -> int:
        """
        Get the recipe ID.

        Returns:
            The recipe ID.
        """
        return self._recipe.id
        
    def get_added_ingredient(self) -> list:
        """
        Get the added ingredient details.

        Returns:
            A list containing the name, quantity, and calories of the added ingredient.
        """
        name = self.name_entry.get()
        quantity = self.quantity_entry.get()
        calories = self.calories_entry.get()
        return [name, quantity, calories]
    
    def _clear_page(self) -> None:
        """
        Clear the page.
        """
        self.name_entry.delete(0, tkc.END)
        self.quantity_entry.delete(0, tkc.END)
        self.calories_entry.delete(0, tkc.END)
        
    def refresh_page(self, recipe: Recipe) -> None:
        """
        Refresh the page with a new recipe.

        Args:
            recipe: The new recipe object.
        """
        self._clear_page()
        self._set_recipe(recipe)