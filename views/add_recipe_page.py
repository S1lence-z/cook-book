# add_recipe_page.py
import tkinter as tk
from .page_abstract_class import Page

class AddRecipePage(tk.Frame, Page):
    def __init__(self, parent: tk.Frame, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_ui()
        
    def create_ui(self):
        # Add recipe button
        button_list_frame = tk.Frame(self, bg="blue")
        button_list_frame.pack()
        button = tk.Button(button_list_frame, text="Save")
        button.pack()