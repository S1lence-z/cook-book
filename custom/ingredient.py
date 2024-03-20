class Ingredient:
    def __init__(self, ing_id: int, recipe_id: int, name: str, quantity: str, calories: int) -> None:
        """
        Initializes an Ingredient object.

        Args:
            ing_id (int): The ID of the ingredient.
            recipe_id (int): The ID of the recipe this ingredient belongs to.
            name (str): The name of the ingredient.
            quantity (str): The quantity of the ingredient.
            calories (int): The number of calories in the ingredient.
        """
        self.ingredient_id = ing_id
        self.recipe_id = recipe_id
        self.name = name
        self.quantity = quantity
        self.calories = calories