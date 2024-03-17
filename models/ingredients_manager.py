from custom import *

class IngredientsManager:
    def __init__(self, db_connection):
        """
        Initializes an IngredientsManager object.

        Args:
            db_connection: The database connection object.
        """
        self.db_connection = db_connection
        self.cursor = db_connection.cursor()
        self.queries = {
            "GetIngredientsByRecipeId": "SELECT * FROM ingredients WHERE recipe_id = ?"
        }
        
    def get_ingredients_by_recipe_id(self, recipe_id: int) -> list[Ingredient]:
        """
        Retrieves all ingredients from the database.

        Returns:
            A list of Ingredient objects representing all the ingredients in the database.
        """
        all_ingredients = []
        self.cursor.execute(self.queries["GetAllIngredients"], (recipe_id,))
        all_ingredients_raw = self.cursor.fetchall()
        for ingredient in all_ingredients_raw:
            id, recipe_id, name, quantity, calories = ingredient
            all_ingredients.append(Ingredient(id, recipe_id, name, quantity, calories))
        return all_ingredients