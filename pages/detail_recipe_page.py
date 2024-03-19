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
        """Create the user interface."""
        self.font = ("Arial", 12)
        self.header = tkc.CTkLabel(self, text="Recipe Detail Page", font=self.font + ("bold",))
        self.header.grid(row=0, column=0, columnspan=3, pady=10)
        # Title
        self.title_label = tkc.CTkLabel(self, text="Title", font=self.font + ("bold",))
        self.title_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        self.title_value = tkc.CTkLabel(self, font=self.font)
        self.title_value.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)
        # Description
        self.description_label = tkc.CTkLabel(self, text="Description", font=self.font + ("bold",))
        self.description_label.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        self.description_value = tkc.CTkLabel(self, font=self.font)
        self.description_value.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
        # Prep Time
        self.prep_time_label = tkc.CTkLabel(self, text="Prep Time", font=self.font + ("bold",))
        self.prep_time_label.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)
        self.prep_time_value = tkc.CTkLabel(self, font=self.font)
        self.prep_time_value.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)
        # Cook Time
        self.cook_time_label = tkc.CTkLabel(self, text="Cook Time", font=self.font + ("bold",))
        self.cook_time_label.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)
        self.cook_time_value = tkc.CTkLabel(self, font=self.font)
        self.cook_time_value.grid(row=4, column=1, sticky="nsew", padx=10, pady=5)
        # Category
        self.category_label = tkc.CTkLabel(self, text="Category", font=self.font + ("bold",))
        self.category_label.grid(row=5, column=0, sticky="nsew", padx=10, pady=5)
        self.category_value = tkc.CTkLabel(self, font=self.font)
        self.category_value.grid(row=5, column=1, sticky="nsew", padx=10, pady=5)
        # Instructions
        self.instructions_label = tkc.CTkLabel(self, text="Instructions", font=self.font + ("bold",))
        self.instructions_label.grid(row=6, column=0, sticky="nsew", padx=10, pady=5)
        self.instructions_value = tkc.CTkLabel(self, font=self.font)
        self.instructions_value.grid(row=6, column=1, sticky="nsew", padx=10, pady=5)
        # Back button
        self.back_btn = tkc.CTkButton(self, text="Back")
        self.back_btn.grid(row=7, column=0, pady=10, padx=10, sticky="nsew")
        # Show ingredients button
        self.show_ingredients_btn = tkc.CTkButton(self, text="Show Ingredients")
        self.show_ingredients_btn.grid(row=7, column=1, pady=10, padx=10, sticky="nsew")
        # Edit button
        self.edit_btn = tkc.CTkButton(self, text="Edit")
        self.edit_btn.grid(row=7, column=2, pady=10, padx=10, sticky="nsew")

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