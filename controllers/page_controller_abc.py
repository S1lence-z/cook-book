# page_controller_abc.py
import tkinter as tk
from abc import ABC, abstractmethod

class PageController:
    @abstractmethod
    def _add_functionality(self):
        pass