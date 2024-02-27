# edit_recipe_page.py
import tkinter as tk
from views.page_abstract_class import Page

class EditRecipePage(tk.Frame, Page):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._create_ui()
    
    def _create_ui(self):
        # Add recipe button
        button_list_frame = tk.Frame(self, bg="blue")
        button_list_frame.pack()
        button = tk.Button(button_list_frame, text="Save")
        button.pack()