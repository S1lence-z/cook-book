# search_bar.py
import tkinter as tk
import ttkbootstrap as tkb

class SearchBar(tk.Entry):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.search_query = self._create_search_query()
        
    def _create_search_query(self) -> tk.StringVar:
        search_query = tk.StringVar()
        return search_query
    
    def get_query(self) -> str:
        return self.get()