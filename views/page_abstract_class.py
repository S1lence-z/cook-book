# page_abstract_class.py
from abc import ABC, abstractmethod

class Page(ABC):
    @abstractmethod
    def create_ui(self) -> None:
        pass