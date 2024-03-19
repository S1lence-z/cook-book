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
        self._recipe_title: str = ""
        self._ingredients_to_display: list[Ingredient] = []
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
        Create the user interface elements for the Ingredients Page with a modern look.
        """
        # Font and color settings
        font_family = "Segoe UI"
        base_font_size = 18
        header_font_size = 28
        primary_color = "#4A90E2"  # Blue shade for primary actions
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

        # Generate PDF button in sidebar
        self.generate_pdf_btn = tkc.CTkButton(self.sidebar_frame, text="Generate PDF", font=font_settings, fg_color="green")
        self.generate_pdf_btn.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Cancel button in sidebar
        self.cancel_btn = tkc.CTkButton(self.sidebar_frame, text="Cancel", font=font_settings, fg_color="red")
        self.cancel_btn.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    def set_ingredients_to_display(self, ingredients: list[Ingredient], recipe_name: str) -> None:
        """
        Set the ingredients to display.

        Args:
            ingredients: The ingredients to display.
            recipe_name: The name of the recipe.
        """
        self._ingredients_to_display = ingredients
        self._recipe_title = recipe_name
        self._fill_the_ingredients_page()
        
    def clear_page(self) -> None:
        """
        Clear the page.
        """
        self.ingredients_list.clear()
        
    def _fill_the_ingredients_page(self) -> None:
        """
        Fill the ingredients page with the given recipe.
        """
        self.ingredients_list_label.configure(text=f"Ingredients of {self._recipe_title}")
        self.ingredients_list.populate(self._ingredients_to_display)
        
    def get_ingredients_list(self) -> list[Ingredient]:
        """
        Get the ingredients list.

        Returns:
            The ingredients list.
        """
        return self._ingredients_to_display
    
    def get_recipe_title(self) -> str:
        """
        Get the recipe title.

        Returns:
            The recipe title.
        """
        return self._recipe_title