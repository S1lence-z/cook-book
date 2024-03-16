# recipe_list.py
import tkinter as tk
from custom.recipe import Recipe

class RecipeList(tk.Listbox):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._db_recipes: list[Recipe] = []
        self._shown_recipes: list[Recipe] = []
        
    def populate(self, list_of_items: list[Recipe]) -> None:
        self._db_recipes = list_of_items
        for item in self._db_recipes:
            self._insert(item)
            
    def curselection(self) -> int:
        index_of_select_item = super().curselection()
        recipe = self._shown_recipes[index_of_select_item[0]]
        return recipe.id
    
    def clear(self) -> None:
        self._clear_shown_recipes()
        self.delete(0, tk.END)   
    
    def filter_recipes(self, search_query: str) -> None:
        self.clear()
        if search_query == "":
            self.populate(self._db_recipes)
            return
        for recipe in self._db_recipes:
            if search_query.lower() in recipe.title.lower():
                self._insert(recipe)
                
    def _add_to_shown_recipes(self, recipe: Recipe) -> None:
        self._shown_recipes.append(recipe)
        
    def _clear_shown_recipes(self) -> None:
        self._shown_recipes.clear()
        
    def _insert(self, item: Recipe) -> None:
        self._add_to_shown_recipes(item)
        self.insert(tk.END, item.title)