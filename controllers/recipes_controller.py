# recipes_controller.py
import tkinter as tk
from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *

class RecipesController(PageController):
    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.pages["recipesPage"]
        self.__setup_page()
        
    def __setup_page(self):
        self._bind_buttons()
        self.frame.refresh_page(self.model.get_all_recipes())
    
    def _bind_buttons(self):
        self.frame.add_btn.config(command=self._add_recipe)
        self.frame.delete_btn.config(command=self._delete_recipe, state=tk.DISABLED)
        self.frame.edit_btn.config(command=self._edit_recipe, state=tk.DISABLED)
        self.frame.detail_btn.config(command=self._show_detail_recipe, state=tk.DISABLED)
        self.frame.recipe_list.bind("<<ListboxSelect>>", self.frame.update_buttons_visibility)
        # Bind search bar
        self.frame.search_bar.bind("<KeyRelease>", self._search_recipes)
        
    def _add_recipe(self) -> None:
        self.view.raise_page("addRecipe")
    
    def _delete_recipe(self) -> None:
        selected_recipe_id = self.frame.recipe_list.curselection()
        self.model.delete_recipe_by_id(selected_recipe_id)
        self.frame.refresh_page(self.model.get_all_recipes())
        print(f"Recipe with id={selected_recipe_id} deleted")
    
    def _edit_recipe(self):
        selected_recipe_id = self.frame.recipe_list.curselection()
        recipe_to_edit = self.model.get_recipe_by_id(selected_recipe_id)
        edit_page = self.view.pages["editRecipe"]
        edit_page.set_recipe_to_edit(recipe_to_edit)
        self.view.raise_page("editRecipe")
        
    def _show_detail_recipe(self) -> None:
        selected_recipe_id = self.frame.recipe_list.curselection()
        recipe_to_display = self.model.get_recipe_by_id(selected_recipe_id)
        detail_page = self.view.pages["detailRecipe"]
        detail_page.set_recipe_to_display(recipe_to_display)
        self.view.raise_page("detailRecipe")
        
    def _search_recipes(self, event) -> None:
        search_query = self.frame.search_bar.get_query()
        self.frame.recipe_list.filter_recipes(search_query)
        self.frame.update_buttons_visibility("<<ListboxSelect>>")