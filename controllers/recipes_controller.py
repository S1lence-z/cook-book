import tkinter as tk
from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *

class RecipesController(PageController):
    """
    Controller class for managing the recipes page.
    """

    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        """
        Initialize the RecipesController.

        Args:
            model (DatabaseManager): The database manager object.
            view (MainView): The main view object.
        """
        self.model = model
        self.view = view
        self.frame = self.view.pages["recipesPage"]
        self._setup_page()

    def _setup_page(self):
        """
        Set up the recipes page by binding buttons and refreshing the page.
        """
        self._bind_buttons()
        self.frame.refresh_page(self.model.get_all_recipes())

    def _bind_buttons(self):
        """
        Bind the buttons on the recipes page to their respective functions.
        """
        self.frame.add_btn.configure(command=self._add_recipe)
        self.frame.delete_btn.configure(command=self._delete_recipe, state=tk.DISABLED)
        self.frame.edit_btn.configure(command=self._edit_recipe, state=tk.DISABLED)
        self.frame.detail_btn.configure(command=self._show_detail_recipe, state=tk.DISABLED)
        self.frame.add_ingredient_btn.configure(command=self._add_ingredient)
        self.frame.recipe_list.bind("<<ListboxSelect>>", self.frame.update_buttons_visibility)
        self.frame.search_bar.bind("<KeyRelease>", self._search_recipes)

    def _add_recipe(self) -> None:
        """
        Open the add recipe page.
        """
        self.view.pages["addRecipe"].refresh_page()
        self.view.raise_page("addRecipe")

    def _delete_recipe(self) -> None:
        """
        Delete the selected recipe from the database and refresh the page.
        """
        selected_recipe_id = self.frame.recipe_list.curselection()
        self.model.delete_recipe_by_id(selected_recipe_id)
        self.frame.refresh_page(self.model.get_all_recipes())
        print(f"Recipe with id={selected_recipe_id} deleted")

    def _edit_recipe(self):
        """
        Open the edit recipe page with the selected recipe pre-filled.
        """
        selected_recipe_id = self.frame.recipe_list.curselection()
        recipe_to_edit = self.model.get_recipe_by_id(selected_recipe_id)
        self.view.pages["editRecipe"].refresh_page(recipe_to_edit)
        self.view.raise_page("editRecipe")

    def _show_detail_recipe(self) -> None:
        """
        Open the detail recipe page with the selected recipe displayed.
        """
        selected_recipe_id = self.frame.recipe_list.curselection()
        recipe_to_display = self.model.get_recipe_by_id(selected_recipe_id)
        self.view.pages["detailRecipe"].refresh_page(recipe_to_display)
        self.view.raise_page("detailRecipe")

    def _search_recipes(self, event) -> None:
        """
        Filter the recipes list based on the search query and update the buttons visibility.
        """
        search_query = self.frame.search_bar.get_query()
        self.frame.recipe_list.filter_recipes(search_query)
        self.frame.update_buttons_visibility("<<ListboxSelect>>")
        
    def _add_ingredient(self) -> None:
        """
        Open the add ingredient page with the selected recipe pre-filled.
        """
        selected_recipe_id = self.frame.recipe_list.curselection()
        recipe_to_add_ingredient = self.model.get_recipe_by_id(selected_recipe_id)
        self.view.pages["addIngredient"].refresh_page(recipe_to_add_ingredient)
        self.view.raise_page("addIngredient")