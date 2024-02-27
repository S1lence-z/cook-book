# page_abstract_class.py
import tkinter as tk
from abc import ABC, abstractmethod

class Page(ABC):
    @abstractmethod
    def _create_ui(self) -> None:
        pass