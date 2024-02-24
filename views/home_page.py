# home_page.py
import tkinter as tk
from .custom_window import AppWindow
from .page_abstract_class import Page

class HomePage(tk.Frame, Page):
    def __init__(self, parent: tk.Frame, controller) -> None:
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_ui()
        
    def create_ui(self):
        self.config(bg="blue")
        # List of recipes
        recipes_frame = tk.Frame(self, bg="red")
        recipes_frame.pack(pady=100)
        recipes_list = tk.Listbox(recipes_frame, bg="green")
        recipes_list.pack(fill=tk.BOTH, expand=True)
        # Button
        button = tk.Button(recipes_frame, text="Test More")
        button.pack()