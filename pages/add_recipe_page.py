import customtkinter as tkc
from custom import *

class AddRecipePage(tkc.CTkFrame, Page):
    """
    A class representing the Add Recipe Page.

    This class inherits from tkc.CTkFrame and Page classes.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize the AddRecipePage object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._format_frame()
        self._create_ui()
        
    def _format_frame(self) -> None:
        """
        Format the frame layout.
        """
        for i in range(2):
            self.grid_columnconfigure(i, weight=1)
        for i in range(3):
            self.grid_rowconfigure(i, weight=1)
    
    def _create_ui(self) -> None:
        """
        Create the user interface elements for the 'Add Recipe Page' with a modern look.
        """
        # Font and color settings
        font_family = "Segoe UI"
        base_font_size = 18
        header_font_size = 28
        font_settings = (font_family, base_font_size)
        header_font_settings = (font_family, header_font_size)

        # Header label
        self.header = tkc.CTkLabel(self, text="Add Recipe Page", font=header_font_settings)
        self.header.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=20, pady=10)

        # Title entry section
        self.title_label = tkc.CTkLabel(self, text="Title", font=font_settings)
        self.title_label.grid(row=1, column=0, sticky="e", padx=20, pady=10)
        self.title_entry = tkc.CTkEntry(self, font=font_settings)
        self.title_entry.grid(row=1, column=1, columnspan=3, sticky="ew", padx=20, pady=10)

        # Sidebar frame for buttons
        self.sidebar_frame = tkc.CTkFrame(self)
        self.sidebar_frame.grid(row=0, column=4, rowspan=3, sticky="nsew", padx=20, pady=10)

        # Add button in sidebar to maintain layout consistency
        self.add_btn = tkc.CTkButton(self.sidebar_frame, text="Add", font=font_settings, fg_color="green")
        self.add_btn.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Cancel button in sidebar
        self.cancel_btn = tkc.CTkButton(self.sidebar_frame, text="Cancel", font=font_settings, fg_color="red")  # Assuming cancel is a secondary/danger action
        self.cancel_btn.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
    def _clear_add_page(self) -> None:
        """
        Clear the input fields on the Add Recipe Page.
        """
        # Clear the title entry
        self.title_entry.delete(0, tkc.END)
        
    def get_added_recipe(self) -> str:
        """
        Get the added recipe details from the input fields.

        Returns:
            str: The title of the added recipe.
        """
        title = self.title_entry.get()
        self._clear_add_page()
        return title