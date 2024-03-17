import tkinter as tk
import ttkbootstrap as tkb
from custom import *

class RecipesPage(tk.Frame, Page):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._format_frame()
        self._create_ui()
        
    def _format_frame(self) -> None:
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)

    def _create_ui(self) -> None:
        # Font settings
        font_family = "Arial"
        font_size = 22
        font_settings = (font_family, font_size)
        
        # Header label
        self.header = tkb.Label(self, text="Recipes Page", font=(font_family, 24), bootstyle=tkb.ACTIVE, anchor="center") # type: ignore
        self.header.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=5)
        
        # Search bar
        self.search_bar_label = tkb.Label(self, text="Search by title:", font=font_settings, bootstyle=tkb.ACTIVE) # type: ignore
        self.search_bar_label.grid(row=1, column=0, padx=10, pady=5)
        self.search_bar = SearchBar(self, font=font_settings)
        self.search_bar.grid(row=1, column=1, columnspan=2, sticky="nsew", padx=10, pady=5)
        
        # Recipe list
        self.recipe_list = RecipeList(self, font=(font_family, 18))
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
        
    def _clear_search_bar(self) -> None:
        self.search_bar.delete(0, tk.END)
        
    def refresh_page(self, all_recipes: list[Recipe]) -> None:
        self._clear_search_bar()
        self._update_recipe_list(all_recipes)
        self.update_buttons_visibility("<<ListboxSelect>>")