import tkinter as tk
import ttkbootstrap as tkb
from custom import *

class HomePage(tk.Frame, Page):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._format_frame()
        self._create_ui()
        
    def _format_frame(self) -> None:
        # Center the content
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # Configure column weights to make buttons split equally
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def _create_ui(self) -> None:
        # Header label
        self.header = tkb.Label(self, text="Home Page", font=("Arial", 24), bootstyle=tkb.ACTIVE, anchor="center") # type: ignore
        self.header.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=5)
        
        # Search bar
        self.search_bar_label = tkb.Label(self, text="Search by title:", font=("Arial", 26), bootstyle=tkb.ACTIVE) # type: ignore
        self.search_bar_label.grid(row=1, column=0, padx=10, pady=5)
        self.search_bar = SearchBar(self, font=("Arial", 26))
        self.search_bar.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=10, pady=5)
        
        # Recipe list
        self.recipe_list = RecipeList(self, font=("Arial", 26))
        self.recipe_list.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=10, pady=5)
        
        # Add Recipe button
        self.add_btn = tkb.Button(self, text="Add Recipe", bootstyle=tkb.SUCCESS) # type: ignore
        self.add_btn.grid(row=3, column=0, sticky="nsew", padx=10, pady=5, ipady=15)
        
        # Delete Recipe button
        self.delete_btn = tkb.Button(self, text="Delete Recipe", bootstyle=tkb.DANGER) # type: ignore
        self.delete_btn.grid(row=3, column=1, sticky="nsew", padx=10, pady=5, ipady=15)
        
        # Edit Recipe button
        self.edit_btn = tkb.Button(self, text="Edit Recipe", bootstyle=tkb.PRIMARY) # type: ignore
        self.edit_btn.grid(row=3, column=2, sticky="nsew", padx=10, pady=5, ipady=15)
        
        # Show Recipe button
        self.detail_btn = tkb.Button(self, text="Show Recipe", bootstyle=tkb.INFO) #type: ignore
        self.detail_btn.grid(row=4, column=0, columnspan=3, sticky="nsew", padx=10, pady=5, ipady=15)

    def update_buttons_visibility(self, event: str) -> None:
        delete_btn = self.delete_btn
        edit_btn = self.edit_btn
        detail_btn = self.detail_btn
        recipe_list = self.recipe_list
        buttons_to_update = [delete_btn, edit_btn, detail_btn]
        # Enable selected buttons if a recipe is selected, else disable it
        for button in buttons_to_update:
            try:
                button.config(state=tk.NORMAL) if recipe_list.curselection() else button.config(state=tk.DISABLED)
            except IndexError:
                button.config(state=tk.DISABLED)
                recipe_list.selection_clear(0, tk.END)

    def _update_recipe_list(self, new_list: list[Recipe]) -> None:
        self.recipe_list.clear()
        self.recipe_list.populate(new_list)
        
    def refresh_page(self, all_recipes: list[Recipe]) -> None:
        self._update_recipe_list(all_recipes)
        self.update_buttons_visibility("<<ListboxSelect>>")