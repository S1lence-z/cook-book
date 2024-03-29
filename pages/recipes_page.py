import customtkinter as tkc
from custom import *

class RecipesPage(tkc.CTkFrame, Page):
    """A class representing the Recipes Page."""

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the RecipesPage.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._format_frame()
        self._create_ui()

    def _format_frame(self) -> None:
        """
        Format the frame.

        Configures the grid columns and rows for the frame.
        """
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)

    def _create_ui(self) -> None:
        """
        Create the user interface.

        Sets up the header label, search bar, recipe list, buttons, and sidebar with a modern look.
        """
        # Font and color settings
        font_family = "Segoe UI"
        base_font_size = 18
        header_font_size = 28
        font_settings = (font_family, base_font_size)
        header_font_settings = (font_family, header_font_size)

        # Header label
        self.header = tkc.CTkLabel(self, text="Recipes Page", font=header_font_settings)
        self.header.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=20, pady=10)

        # Search bar
        self.search_bar_label = tkc.CTkLabel(self, text="Search by title:", font=header_font_settings)
        self.search_bar_label.grid(row=1, column=0, sticky="", padx=20, pady=10)
        self.search_bar = SearchBar(self, font=font_settings)
        self.search_bar.grid(row=1, column=1, columnspan=3, sticky="ew", padx=20, pady=10)

        # Recipe list
        self.recipe_list = RecipeList(self, font=(font_family, 16))
        self.recipe_list.grid(row=2, column=0, columnspan=4, sticky="nsew", padx=20, pady=10)

        # Sidebar frame for buttons
        self.sidebar_frame = tkc.CTkFrame(self)
        self.sidebar_frame.grid(row=0, column=4, rowspan=4, sticky="nsew", padx=20, pady=10)

        # Sidebar buttons
        self.add_btn = tkc.CTkButton(self.sidebar_frame, text="Add Recipe", font=font_settings, fg_color="green")
        self.add_btn.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        self.add_ingredient_btn = tkc.CTkButton(self.sidebar_frame, text="Add Ingredient", font=font_settings, fg_color="green")
        self.add_ingredient_btn.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.delete_btn = tkc.CTkButton(self.sidebar_frame, text="Delete Recipe", font=font_settings, fg_color="red")
        self.delete_btn.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

        self.edit_btn = tkc.CTkButton(self.sidebar_frame, text="Edit Recipe", font=font_settings, fg_color="blue")
        self.edit_btn.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

        self.detail_btn = tkc.CTkButton(self.sidebar_frame, text="Show Recipe", font=font_settings, fg_color="blue")
        self.detail_btn.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)

    def update_buttons_visibility(self, event: str) -> None:
        """
        Update the visibility of buttons.

        Args:
            event (str): The event that triggered the update.
        """
        delete_btn = self.delete_btn
        edit_btn = self.edit_btn
        detail_btn = self.detail_btn
        recipe_list = self.recipe_list
        add_ingredient_btn = self.add_ingredient_btn
        buttons_to_update = [delete_btn, edit_btn, detail_btn, add_ingredient_btn]
        # Enable selected buttons if a recipe is selected, else disable it
        for button in buttons_to_update:
            try:
                button.configure(state=tkc.NORMAL) if recipe_list.curselection() else button.configure(state=tkc.DISABLED)
            except IndexError:
                button.configure(state=tkc.DISABLED)
                recipe_list.selection_clear(0, tkc.END)

    def _update_recipe_list(self, new_list: list[Recipe]) -> None:
        """
        Update the recipe list.

        Args:
            new_list (list[Recipe]): The new list of recipes.
        """
        self.recipe_list.clear()
        self.recipe_list.populate(new_list)

    def _clear_search_bar(self) -> None:
        """
        Clear the search bar.
        """
        self.search_bar.delete(0, tkc.END)

    def refresh_page(self, all_recipes: list[Recipe]) -> None:
        """
        Refresh the page.

        Args:
            all_recipes (list[Recipe]): The list of all recipes.
        """
        self._clear_search_bar()
        self._update_recipe_list(all_recipes)
        self.update_buttons_visibility("<<ListboxSelect>>")