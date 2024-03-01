# home_controller.py
import tkinter as tk
from models.database_manager import DatabaseManager
from controllers import *

class HomeController(PageController):
    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.pages["home"]
        self._setup_page()
        
    def _setup_page(self):
        self._bind_buttons()
        self._bind_recipe_list()
    
    def _bind_buttons(self):
        self.frame.add_btn.config(command=self._add_recipe)
        self.frame.delete_btn.config(command=self._delete_recipe, state=tk.DISABLED)
        self.frame.edit_btn.config(command=self._edit_recipe)
        
    def _bind_recipe_list(self):
        setup_lst = self.model.get_all_recipes()
        self.frame.update_recipe_list(setup_lst)
        self.frame.recipe_list.bind("<<ListboxSelect>>", self.frame.update_delete_btn_state)
        
    def _add_recipe(self) -> None:
        self.view.raise_page("addRecipe")
    
    def _delete_recipe(self) -> None:
        selected_recipe_id = self.frame.recipe_list.curselection()
        self.model.delete_recipe_by_id(selected_recipe_id)
        new_lst = self.model.get_all_recipes()
        self.frame.update_recipe_list(new_lst)
        print(f"Recipe with id={selected_recipe_id} deleted")
    
    def _edit_recipe(self):
        self.view.raise_page("editRecipe")