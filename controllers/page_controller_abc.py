# page_controller_abc.py
import tkinter as tk
from abc import ABC, abstractmethod

class PageController:
    @abstractmethod
    def _setup_page(self) -> None:
        """ Sets up the whole page. """
        pass
    
    @abstractmethod
    def _bind_buttons(self) -> None:
        """ Binds methods to buttons for their functionality. """
        pass