# page_controller_abc.py
from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class PageController(ABC):
    """Abstract base class for page controllers."""

    @abstractmethod
    def __setup_page(self) -> None:
        """Sets up the whole page."""
        pass
    
    @abstractmethod
    def _bind_buttons(self) -> None:
        """Binds methods to buttons for their functionality."""
        pass