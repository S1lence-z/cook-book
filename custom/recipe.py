from custom.recipe_category import RecipeCategory

class Recipe:
    def __init__(self, id: int, title: str, description: str, prep_time: int, cook_time: int, instructions: str, category: RecipeCategory) -> None:
        """
        Initialize a Recipe object.

        Args:
            id (int): The unique identifier for the recipe.
            title (str): The title of the recipe.
            description (str): A brief description of the recipe.
            prep_time (int): The preparation time in minutes.
            cook_time (int): The cooking time in minutes.
            instructions (str): The instructions for preparing the recipe.
            category (RecipeCategory): The category of the recipe.

        Returns:
            None
        """
        self.id = id
        self.title = title
        self.description = description
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.instructions = instructions
        self.category = category