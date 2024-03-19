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
        """Creates the user interface elements for the Edit Recipe Page."""
        self.header = tkc.CTkLabel(self, text="Edit Recipe Page", font=("Arial", 24), anchor="center")
        self.header.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=5)

        # Title
        self.title_label = tkc.CTkLabel(self, text="Title", font=("Arial", 12))
        self.title_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        self.title_entry = tkc.CTkEntry(self)
        self.title_entry.grid(row=1, column=1, columnspan=3, sticky="nsew", padx=10, pady=5)

        # Description
        self.description_label = tkc.CTkLabel(self, text="Description", font=("Arial", 12))
        self.description_label.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        self.description_text = tkc.CTkTextbox(self, height=10)
        self.description_text.grid(row=2, column=1, columnspan=3, sticky="nsew", padx=10, pady=5)

        # Prep Time
        self.prep_time_label = tkc.CTkLabel(self, text="Prep Time (minutes)", font=("Arial", 12))
        self.prep_time_label.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)
        self.prep_time_entry = tkc.CTkEntry(self)
        self.prep_time_entry.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

        # Cook Time
        self.cook_time_label = tkc.CTkLabel(self, text="Cook Time (minutes)", font=("Arial", 12))
        self.cook_time_label.grid(row=3, column=2, sticky="nsew", padx=10, pady=5)
        self.cook_time_entry = tkc.CTkEntry(self)
        self.cook_time_entry.grid(row=3, column=3, sticky="nsew", padx=10, pady=5)

        # Instructions
        self.instructions_label = tkc.CTkLabel(self, text="Instructions", font=("Arial", 12))
        self.instructions_label.grid(row=5, column=0, sticky="nsew", padx=10, pady=5)
        self.instructions_text = tkc.CTkTextbox(self, height=10)
        self.instructions_text.grid(row=5, column=1, columnspan=3, sticky="nsew", padx=10, pady=5)
        
        # Category
        self.category_label = tkc.CTkLabel(self, text="Category", font=("Arial", 12))
        self.category_label.grid(row=4, column=0, sticky="nsew", padx=10, pady=5)
        self.category_entry = tkc.CTkEntry(self)
        self.category_entry.grid(row=4, column=1, columnspan=3, sticky="nsew", padx=10, pady=5)

        # Save button
        self.save_btn = tkc.CTkButton(self, text="Save")
        self.save_btn.grid(row=6, column=1, columnspan=2, sticky="nsew", padx=10, pady=5, ipady=15)
        # Cancel button
        self.cancel_btn = tkc.CTkButton(self, text="Cancel")
        self.cancel_btn.grid(row=6, column=3, sticky="nsew", padx=10, pady=5, ipady=15)

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