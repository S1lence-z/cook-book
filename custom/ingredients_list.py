import tkinter as tk
from custom.ingredient import Ingredient

class IngredientsList(tk.Listbox):
    """
    A custom Listbox widget for displaying ingredients.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the IngredientsList.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._db_ingredients: list[Ingredient] = []
        self._shown_ingredients: list[Ingredient] = []

    def populate(self, list_of_items: list[Ingredient]) -> None:
        """
        Populate the IngredientsList with a list of ingredients.

        Args:
            list_of_items (list[Ingredient]): The list of ingredients to populate the IngredientsList with.
        """
        self._db_ingredients = list_of_items
        for item in self._db_ingredients:
            self._insert(item)

    def curselection(self) -> int:
        """
        Get the ID of the currently selected ingredient.

        Returns:
            int: The ID of the currently selected ingredient.
        """
        index_of_selected_item = super().curselection()
        ingredient = self._shown_ingredients[index_of_selected_item[0]]
        return ingredient.ingredient_id

    def clear(self) -> None:
        """
        Clear the IngredientsList.
        """
        self._clear_shown_ingredients()
        self.delete(0, tk.END)
        
    def _add_to_shown_ingredients(self, ingredient: Ingredient) -> None:
        """
        Add an ingredient to the list of shown ingredients.

        Args:
            ingredient (Ingredient): The ingredient to add.
        """
        self._shown_ingredients.append(ingredient)
        
    def _clear_shown_ingredients(self) -> None:
        """
        Clear the list of shown ingredients.
        """
        self._shown_ingredients.clear()

    def _insert(self, item: Ingredient) -> None:
        """
        Insert an ingredient into the IngredientsList.

        Args:
            item (Ingredient): The ingredient to insert.
        """
        self.insert(tk.END, item.name)
        self._add_to_shown_ingredients(item)