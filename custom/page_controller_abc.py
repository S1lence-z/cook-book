from abc import ABC, abstractmethod

class PageController(ABC):
    """Abstract base class for page controllers."""

    @abstractmethod
    def _setup_page(self) -> None:
        """Sets up the whole page.
        
        This method should be implemented by subclasses to set up the entire page.
        """
        pass
    
    @abstractmethod
    def _bind_buttons(self) -> None:
        """Binds methods to buttons for their functionality.
        
        This method should be implemented by subclasses to bind methods to buttons for their functionality.
        """
        pass