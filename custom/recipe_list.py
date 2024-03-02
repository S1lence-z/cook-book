# recipe_list.py
import tkinter as tk
from custom.recipe import Recipe

class RecipeList(tk.Listbox):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._db_recipes: list[Recipe] = []
        
    def populate(self, list_of_items: list[Recipe]) -> None:
        self._db_recipes = list_of_items
        for item in self._db_recipes:
            self.insert(tk.END, item.title)
            
    def clear(self) -> None:
        self.delete(0, tk.END)
            
    def curselection(self) -> int:
        index_of_select_item = super().curselection()
        recipe = self._db_recipes[index_of_select_item[0]]
        return recipe.id