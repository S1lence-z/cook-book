import customtkinter as tkc
from custom import *

class EditRecipePage(tkc.CTkFrame, Page):
    """A class representing the Edit Recipe Page.

    This page allows the user to edit a recipe's details such as title, description, prep time, cook time, and instructions.

    Attributes:
        _recipe_to_edit (Recipe): The recipe object to be edited.
    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the EditRecipePage class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self._recipe_to_edit: Recipe
        self._format_frame()
        self._create_ui()
        
    def _format_frame(self) -> None:
        """Formats the frame by configuring row and column weights."""
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)

    def _create_ui(self) -> None:
        """Creates the user interface elements for the Edit Recipe Page with a modern look, including a sidebar."""
        # Font and color settings
        font_family = "Segoe UI"
        base_font_size = 18
        header_font_size = 28
        font_settings = (font_family, base_font_size)
        header_font_settings = (font_family, header_font_size)

        # Header label
        self.header = tkc.CTkLabel(self, text="Edit Recipe Page", font=header_font_settings)
        self.header.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)

        # Title
        self.title_label = tkc.CTkLabel(self, text="Title", font=font_settings)
        self.title_label.grid(row=1, column=0, sticky="e", padx=20, pady=10)
        self.title_entry = tkc.CTkEntry(self, font=font_settings)
        self.title_entry.grid(row=1, column=1, columnspan=2, sticky="ew", padx=20, pady=10)

        # Description
        self.description_label = tkc.CTkLabel(self, text="Description", font=font_settings)
        self.description_label.grid(row=2, column=0, sticky="e", padx=20, pady=10)
        self.description_text = tkc.CTkTextbox(self, height=10, font=font_settings)
        self.description_text.grid(row=2, column=1, columnspan=2, sticky="nsew", padx=20, pady=10)

        # Prep Time
        self.prep_time_label = tkc.CTkLabel(self, text="Prep Time (minutes)", font=font_settings)
        self.prep_time_label.grid(row=3, column=0, sticky="e", padx=20, pady=10)
        self.prep_time_entry = tkc.CTkEntry(self, font=font_settings)
        self.prep_time_entry.grid(row=3, column=1, sticky="ew", padx=20, pady=10)

        # Cook Time
        self.cook_time_label = tkc.CTkLabel(self, text="Cook Time (minutes)", font=font_settings)
        self.cook_time_label.grid(row=3, column=2, sticky="e", padx=20, pady=10)
        self.cook_time_entry = tkc.CTkEntry(self, font=font_settings)
        self.cook_time_entry.grid(row=3, column=3, sticky="ew", padx=20, pady=10)

        # Category
        self.category_label = tkc.CTkLabel(self, text="Category", font=font_settings)
        self.category_label.grid(row=4, column=0, sticky="e", padx=20, pady=10)
        self.category_entry = tkc.CTkEntry(self, font=font_settings)
        self.category_entry.grid(row=4, column=1, columnspan=2, sticky="ew", padx=20, pady=10)

        # Instructions
        self.instructions_label = tkc.CTkLabel(self, text="Instructions", font=font_settings)
        self.instructions_label.grid(row=5, column=0, sticky="e", padx=20, pady=10)
        self.instructions_text = tkc.CTkTextbox(self, height=10, font=font_settings)
        self.instructions_text.grid(row=5, column=1, columnspan=2, sticky="nsew", padx=20, pady=10)

        # Sidebar frame for action buttons
        self.sidebar_frame = tkc.CTkFrame(self)
        self.sidebar_frame.grid(row=0, column=4, rowspan=7, sticky="nsew", padx=20, pady=10)

        # Save button in sidebar
        self.save_btn = tkc.CTkButton(self.sidebar_frame, text="Save", font=font_settings, fg_color="green")
        self.save_btn.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Cancel button in sidebar
        self.cancel_btn = tkc.CTkButton(self.sidebar_frame, text="Cancel", font=font_settings, fg_color="red")
        self.cancel_btn.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)


    def set_recipe_to_edit(self, recipe: Recipe):
        """Sets the recipe to be edited.

        Args:
            recipe (Recipe): The recipe object to be edited.
        """
        self._recipe_to_edit = recipe
        self._fill_the_edit_page()
        
    def _clear_edit_page(self):
        """Clears the edit page by resetting the input fields."""
        # Clear the title entry
        self.title_entry.delete(0, tkc.END)
        # Clear the description text.
        self.description_text.delete('1.0', tkc.END)
        # Clear the prep time entry
        self.prep_time_entry.delete(0, tkc.END)
        # Clear the cook time entry
        self.cook_time_entry.delete(0, tkc.END)
        # Clear the instructions text.
        self.instructions_text.delete('1.0', tkc.END)
        # Clear the category entry
        self.category_entry.delete(0, tkc.END)
            
    def _fill_the_edit_page(self) -> None:
        """Fills the edit page with the recipe's current values."""
        self._clear_edit_page()
        # Fill the form with the recipe's current values
        self.title_entry.insert(0, self._recipe_to_edit.title)
        self.description_text.insert(tkc.END, self._recipe_to_edit.description)
        self.prep_time_entry.insert(0, str(self._recipe_to_edit.prep_time))
        self.cook_time_entry.insert(0, str(self._recipe_to_edit.cook_time))
        self.instructions_text.insert(tkc.END, self._recipe_to_edit.instructions)
        self.category_entry.insert(0, self._recipe_to_edit.category.value)
        
    def get_edited_recipe(self):
        """Gets the edited recipe details from the input fields.

        Returns:
            list: A list containing the edited recipe details in the following order:
                [recipe_id, title, description, prep_time, cook_time, instructions, category]
        """
        recipe_id = self._recipe_to_edit.id
        title = self.title_entry.get()
        description = self.description_text.get("1.0", "end-1c")
        prep_time = self.prep_time_entry.get()
        cook_time = self.cook_time_entry.get()
        instructions = self.instructions_text.get("1.0", "end-1c")
        category = self.category_entry.get()
        return [recipe_id, title, description, prep_time, cook_time, instructions, category]