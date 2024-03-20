import customtkinter as tkc
from custom import *

class IngredientsPage(tkc.CTkFrame, Page):
    """
    A class representing the Ingredients Page.

    This class inherits from tkc.CTkFrame and Page classes.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the IngredientsPage object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._recipe: Recipe
        self._recipe_ingredients: list[Ingredient] = []
        self._format_frame()
        self._create_ui()
        
    def _format_frame(self) -> None:
        """
        Format the frame layout.
        """
        for i in range(2):
            self.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
    
    def _create_ui(self) -> None:
        """
        Create the user interface elements for the Ingredients Page with a modern look.
        """
        # Font and color settings
        font_family = "Segoe UI"
        base_font_size = 18
        header_font_size = 28
        font_settings = (font_family, base_font_size)
        header_font_settings = (font_family, header_font_size)

        # Header label
        self.header = tkc.CTkLabel(self, text="Ingredients Page", font=header_font_settings)
        self.header.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20, pady=10)

        # Ingredients List
        self.ingredients_list_label = tkc.CTkLabel(self, text="Ingredients of", font=(font_family, 16))
        self.ingredients_list_label.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=20, pady=10)
        self.ingredients_list = IngredientsList(self, font=font_settings)
        self.ingredients_list.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=20, pady=10)

        # Sidebar frame for buttons
        self.sidebar_frame = tkc.CTkFrame(self)
        self.sidebar_frame.grid(row=0, column=2, rowspan=4, sticky="nsew", padx=20, pady=10)
        
        # Button to add a new ingredient
        self.add_ingredient_btn = tkc.CTkButton(self.sidebar_frame, text="Add Ingredient", font=font_settings, fg_color="blue")
        self.add_ingredient_btn.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        # Delete ingredient
        self.delete_ingredient_btn = tkc.CTkButton(self.sidebar_frame, text="Delete", font=font_settings, fg_color="red")
        self.delete_ingredient_btn.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Generate PDF button in sidebar
        self.generate_pdf_btn = tkc.CTkButton(self.sidebar_frame, text="Generate PDF", font=font_settings, fg_color="green")
        self.generate_pdf_btn.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

        # Cancel button in sidebar
        self.cancel_btn = tkc.CTkButton(self.sidebar_frame, text="Back", font=font_settings, fg_color="red")
        self.cancel_btn.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

    def _set_ingredients_to_display(self, ingredients: list[Ingredient]) -> None:
        """
        Set the ingredients to display.

        Args:
            ingredients: The ingredients to display.
        """
        self._recipe_ingredients = ingredients
        
    def _set_recipe(self, recipe: Recipe) -> None:
        """
        Set the recipe title.

        Args:
            recipe: The recipe title.
        """
        self._recipe = recipe
        
    def _clear_page(self) -> None:
        """
        Clear the page.
        """
        self.ingredients_list_label.configure(text=f"Ingredients of NOT SET")
        self.ingredients_list.clear()
        
    def _fill_the_ingredients_page(self) -> None:
        """
        Fill the ingredients page with the given recipe.
        """
        self.ingredients_list_label.configure(text=f"Ingredients of {self._recipe.title}")
        self.ingredients_list.populate(self._recipe_ingredients)
        
    def get_recipe(self) -> Recipe:
        """
        Get the recipe.

        Returns:
            The recipe.
        """
        return self._recipe
    
    def get_ingredients_list(self) -> list[Ingredient]:
        """
        Get the list of ingredients.

        Returns:
            The list of ingredients.
        """
        return self._recipe_ingredients
    
    def update_buttons_visibility(self, event: str) -> None:
        """
        Update the visibility of buttons.

        Args:
            event (str): The event that triggered the update.
        """
        delete_btn = self.delete_ingredient_btn
        ingredient_list = self.ingredients_list
        buttons_to_update = [delete_btn]
        # Enable selected buttons if a recipe is selected, else disable it
        for button in buttons_to_update:
            try:
                button.configure(state=tkc.NORMAL) if ingredient_list.curselection() else button.configure(state=tkc.DISABLED)
            except IndexError:
                button.configure(state=tkc.DISABLED)
                ingredient_list.selection_clear(0, tkc.END)
    
    def refresh_page(self, recipe_ingredients: list[Ingredient], recipe: Recipe) -> None:
        """
        Refresh the page.

        Args:
            recipe_ingredients: The ingredients of the recipe.
            recipe: The recipe.
        """
        self._clear_page()
        self._set_recipe(recipe)
        self._set_ingredients_to_display(recipe_ingredients)
        self._fill_the_ingredients_page()
        self.update_buttons_visibility("refresh")