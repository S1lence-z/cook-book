# recipe.py
from custom.recipe_category import RecipeCategory

class Recipe:
    def __init__(self, id: int, title: str, description: str, prep_time: int, cook_time: int, instructions: str, category: RecipeCategory)-> None:
        self.id = id
        self.title = title
        self.description = description
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.instructions = instructions
        self.category = category