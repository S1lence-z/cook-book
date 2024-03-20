# page_abstract_class.py
from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Page(ABC):
    """
    Abstract base class representing a page.
    """

    @abstractmethod
    def _create_ui(self) -> None:
        """
        Abstract method to create the user interface for the page.
        """
        pass
    
    @abstractmethod
    def refresh_page(self) -> None:
        """
        Abstract method to refresh the page.
        """
        pass