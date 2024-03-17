import tkinter as tk
from custom.recipe import Recipe

class RecipeList(tk.Listbox):
    """
    A custom Listbox widget for displaying recipes.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the RecipeList.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._db_recipes: list[Recipe] = []
        self._shown_recipes: list[Recipe] = []

    def populate(self, list_of_items: list[Recipe]) -> None:
        """
        Populate the RecipeList with a list of recipes.

        Args:
            list_of_items (list[Recipe]): The list of recipes to populate the RecipeList with.
        """
        self._db_recipes = list_of_items
        for item in self._db_recipes:
            self._insert(item)

    def curselection(self) -> int:
        """
        Get the ID of the currently selected recipe.

        Returns:
            int: The ID of the currently selected recipe.
        """
        index_of_select_item = super().curselection()
        recipe = self._shown_recipes[index_of_select_item[0]]
        return recipe.id

    def clear(self) -> None:
        """
        Clear the RecipeList.
        """
        self._clear_shown_recipes()
        self.delete(0, tk.END)

    def filter_recipes(self, search_query: str) -> None:
        """
        Filter the recipes in the RecipeList based on a search query.

        Args:
            search_query (str): The search query to filter the recipes.
        """
        self.clear()
        if search_query == "":
            self.populate(self._db_recipes)
            return
        for recipe in self._db_recipes:
            if search_query.lower() in recipe.title.lower():
                self._insert(recipe)

    def _add_to_shown_recipes(self, recipe: Recipe) -> None:
        """
        Add a recipe to the list of shown recipes.

        Args:
            recipe (Recipe): The recipe to add.
        """
        self._shown_recipes.append(recipe)

    def _clear_shown_recipes(self) -> None:
        """
        Clear the list of shown recipes.
        """
        self._shown_recipes.clear()

    def _insert(self, item: Recipe) -> None:
        """
        Insert a recipe into the RecipeList.

        Args:
            item (Recipe): The recipe to insert.
        """
        self._add_to_shown_recipes(item)
        self.insert(tk.END, item.title)