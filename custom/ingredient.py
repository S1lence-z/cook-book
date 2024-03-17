class Ingredient:
    def __init__(self, ing_id: int, recipe_id: int, name: str, quantity: str, calories: int) -> None:
        """
        Initializes an Ingredient object.

        Args:
            id: The ingredient's ID.
            name: The ingredient's name.
        """
        self.ingredient_id = ing_id
        self.recipe_id = recipe_id
        self.name = name
        self.quantity = quantity
        self.calories = calories