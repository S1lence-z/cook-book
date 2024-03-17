import tkinter as tk

class SearchBar(tk.Entry):
    """A custom search bar widget."""

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the SearchBar widget.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)

    def get_query(self) -> str:
        """
        Get the current search query.

        Returns:
            str: The current search query.
        """
        return self.get()