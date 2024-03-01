# home_page.py
import tkinter as tk
from views.page_abc import Page
from views.recipe_list import RecipeList
from models.recipe import Recipe

class HomePage(tk.Frame, Page):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._create_ui()
        
    def _create_ui(self):
        self.header = tk.Label(self, text="Home Page")
        self.header.pack()
        # LIST THE EXISTING RECIPES
        self.recipe_list = RecipeList(self)
        self.recipe_list.pack()
        # ALL PAGE BUTTONS
        self.add_btn = tk.Button(self, text="Add Recipe")
        self.add_btn.pack()
        self.delete_btn = tk.Button(self, text="Delete Recipe")
        self.delete_btn.pack()
        self.edit_btn = tk.Button(self, text="Edit Recipe")
        self.edit_btn.pack()
        
    def update_delete_btn_state(self, event: str):
        #? SHOULD THIS BE HERE
        delete_btn = self.delete_btn
        recipe_list = self.recipe_list
        delete_btn.config(state=tk.NORMAL) if recipe_list.curselection() else delete_btn.config(state=tk.DISABLED)
        
    def update_recipe_list(self, new_list: list[Recipe]):
        #? SHOULD THIS BE HERE
        self.recipe_list.clear()
        self.recipe_list.populate(new_list)