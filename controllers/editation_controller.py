from models.database_manager import DatabaseManager
from views.main_view import MainView
from controllers import *
from custom.recipe_category import RecipeCategory
from custom.warning_box import CustomWarningBox

class EditRecipeController(PageController):
    """
    Controller class for the editation page.
    """

    def __init__(self, model: DatabaseManager, view: MainView) -> None:
        """
        Initializes the EditationController.

        Args:
            model (DatabaseManager): The database manager.
            view (MainView): The main view.
        """
        self.model = model
        self.view = view
        self.frame = self.view.pages["editRecipe"]
        self._setup_page()

    def _setup_page(self):
        """
        Sets up the editation page.
        """
        self._bind_buttons()

    def _bind_buttons(self) -> None:
        """
        Binds the buttons to their respective functions.
        """
        self.frame.save_btn.configure(command=self._save_edited_recipe)
        self.frame.cancel_btn.configure(command=self._cancel)
        self.frame.category_options.configure(values=self._get_recipe_categories())
        
    def _get_recipe_categories(self) -> list[RecipeCategory]:
        """
        Gets the recipe categories from the database.

        Returns:
            list[RecipeCategory]: The recipe categories.
        """
        all_categories = []
        for category in RecipeCategory:
            all_categories.append(category.value)
        return all_categories

    def _save_edited_recipe(self):
        """
        Saves the edited recipe.
        """
        recipe_id, title, description, prep_time, cook_time, instructions, category = self.frame.get_edited_recipe()
        if not title:
            warning = CustomWarningBox(self.frame, "Invalid Input", "Please enter a title for the recipe.", "300", "200")
            warning.show()
            return
        
        if not prep_time.isdigit() or not cook_time.isdigit():
            warning = CustomWarningBox(self.frame, "Invalid Input", "Please enter a valid number for prep time and cook time.", "400", "100")
            warning.show()
            return
        
        self.model.update_recipe(recipe_id, title, description, prep_time, cook_time, instructions, category)
        self.view.pages["recipesPage"].refresh_page(self.model.get_all_recipes())
        self.view.raise_page("recipesPage")

    def _cancel(self):
        """
        Cancels the editation and returns to the recipes page.
        """
        self.view.pages["recipesPage"].refresh_page(self.model.get_all_recipes())
        self.view.raise_page("recipesPage")