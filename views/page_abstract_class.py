# page_abstract_class.py
from abc import ABC, abstractmethod
import tkinter as tk
from .custom_window import AppWindow

class Page(ABC):
    def create_page_frame(self, window: AppWindow, bg_color: str):
        # Whole page frame
        page_frame = tk.Frame(window, bg=bg_color)
        page_frame.pack(fill=tk.BOTH, expand=True)
        return page_frame