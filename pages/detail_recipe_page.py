import customtkinter as tkc
from custom import *

class DetailRecipePage(tkc.CTkFrame, Page):
    """A class representing the detail recipe page."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the DetailRecipePage class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._recipe_to_display: Recipe
        self._format_frame()
        self._create_ui()

    def _format_frame(self) -> None:
        """Format the frame."""
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)

    def _create_ui(self) -> None:
        """Create the user interface for the Recipe Detail Page with a modern look, including a sidebar."""
        # Font and color settings
        font_family = "Segoe UI"
        base_font_size = 18
        header_font_size = 28
        primary_color = "#4A90E2"  # Blue shade for primary actions
        font_settings = (font_family, base_font_size)
        header_font_settings = (font_family, header_font_size, "bold")

        # Header label
        self.header = tkc.CTkLabel(self, text="Recipe Detail Page", font=header_font_settings)
        self.header.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=20, pady=10)

        # Title
        self.title_label = tkc.CTkLabel(self, text="Title", font=header_font_settings)
        self.title_label.grid(row=1, column=0, sticky="e", padx=20, pady=10)
        self.title_value = tkc.CTkLabel(self, font=font_settings)
        self.title_value.grid(row=1, column=1, columnspan=2, sticky="ew", padx=20, pady=10)

        # Description
        self.description_label = tkc.CTkLabel(self, text="Description", font=header_font_settings)
        self.description_label.grid(row=2, column=0, sticky="e", padx=20, pady=10)
        self.description_value = tkc.CTkLabel(self, font=font_settings)
        self.description_value.grid(row=2, column=1, columnspan=2, sticky="ew", padx=20, pady=10)

        # Prep Time
        self.prep_time_label = tkc.CTkLabel(self, text="Prep Time", font=header_font_settings)
        self.prep_time_label.grid(row=3, column=0, sticky="e", padx=20, pady=10)
        self.prep_time_value = tkc.CTkLabel(self, font=font_settings)
        self.prep_time_value.grid(row=3, column=1, sticky="ew", padx=20, pady=10)

        # Cook Time
        self.cook_time_label = tkc.CTkLabel(self, text="Cook Time", font=header_font_settings)
        self.cook_time_label.grid(row=4, column=0, sticky="e", padx=20, pady=10)
        self.cook_time_value = tkc.CTkLabel(self, font=font_settings)
        self.cook_time_value.grid(row=4, column=1, sticky="ew", padx=20, pady=10)

        # Category
        self.category_label = tkc.CTkLabel(self, text="Category", font=header_font_settings)
        self.category_label.grid(row=5, column=0, sticky="e", padx=20, pady=10)
        self.category_value = tkc.CTkLabel(self, font=font_settings)
        self.category_value.grid(row=5, column=1, sticky="ew", padx=20, pady=10)

        # Instructions
        self.instructions_label = tkc.CTkLabel(self, text="Instructions", font=header_font_settings)
        self.instructions_label.grid(row=6, column=0, sticky="e", padx=20, pady=10)
        self.instructions_value = tkc.CTkLabel(self, font=font_settings)
        self.instructions_value.grid(row=6, column=1, columnspan=2, sticky="ew", padx=20, pady=10)

        # Sidebar frame for buttons
        self.sidebar_frame = tkc.CTkFrame(self)
        self.sidebar_frame.grid(row=0, column=3, rowspan=8, sticky="nsew", padx=20, pady=10)

        # Action buttons in sidebar
        self.edit_btn = tkc.CTkButton(self.sidebar_frame, text="Edit", font=font_settings, fg_color="blue")
        self.edit_btn.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        self.show_ingredients_btn = tkc.CTkButton(self.sidebar_frame, text="Show Ingredients", font=font_settings, fg_color="blue")
        self.show_ingredients_btn.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        self.back_btn = tkc.CTkButton(self.sidebar_frame, text="Back", font=font_settings, fg_color="red")
        self.back_btn.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

    def set_recipe_to_display(self, recipe: Recipe):
        """Set the recipe to display.

        Args:
            recipe (Recipe): The recipe to display.
        """
        self._recipe_to_display = recipe
        self._fill_the_display_page()

    def clear_page(self):
        """Clear the page."""
        self.title_value.configure(text="")
        self.description_value.configure(text="")
        self.prep_time_value.configure(text="")
        self.cook_time_value.configure(text="")
        self.instructions_value.configure(text="")

    def _fill_the_display_page(self):
        """Fill the display page with recipe details."""
        self.title_value.configure(text=self._recipe_to_display.title)
        self.description_value.configure(text=self._recipe_to_display.description)
        self.prep_time_value.configure(text=f"{self._recipe_to_display.prep_time} minutes")
        self.cook_time_value.configure(text=f"{self._recipe_to_display.cook_time} minutes")
        self.instructions_value.configure(text=self._recipe_to_display.instructions)
        self.category_value.configure(text=self._recipe_to_display.category.value)