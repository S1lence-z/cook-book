from custom import *

class DatabaseManager:
    def __init__(self, db_connection):
        """
        Initializes a DatabaseManager object.

        Args:
            db_connection: The database connection object.
        """
        self.db_connection = db_connection
        self.cursor = db_connection.cursor()
        self.queries = {
            "GetAllRecipes": "SELECT * FROM recipes;",
            "GetRecipeById": "SELECT * FROM recipes WHERE recipe_id = %s;",
            "AddRecipe": "INSERT INTO recipes (title, _description, prep_time, cook_time, instructions) VALUES (%s, %s, %s, %s, %s);",
            "DeleteRecipeById": "DELETE FROM recipes WHERE recipe_id = %s;",
            "UpdateRecipe": "UPDATE recipes SET title = %s, _description = %s, prep_time = %s, cook_time = %s, instructions = %s WHERE recipe_id = %s;"
        }
        
    def get_all_recipes(self) -> list[Recipe]:
        """
        Retrieves all recipes from the database.

        Returns:
            A list of Recipe objects representing all the recipes in the database.
        """
        all_recipes = []
        self.cursor.execute(self.queries["GetAllRecipes"])
        all_recipes_raw = self.cursor.fetchall()
        for recipe in all_recipes_raw:
            id, title, description, prep_time, cook_time, instructions = recipe
            all_recipes.append(Recipe(id, title, description, prep_time, cook_time, instructions))
        return all_recipes
    
    def get_recipe_by_id(self, id: int) -> Recipe:
        """
        Retrieves a recipe from the database by its ID.

        Args:
            id: The ID of the recipe to retrieve.

        Returns:
            A Recipe object representing the retrieved recipe.
        """
        self.cursor.execute(self.queries["GetRecipeById"], (id,))
        recipe = self.cursor.fetchall()
        id, title, description, prep_time, cook_time, instructions = recipe[0]
        return Recipe(id, title, description, prep_time, cook_time, instructions)
            
    def add_recipe(self, title: str):
        """
        Adds a new recipe to the database.

        Args:
            title: The title of the recipe.
        """
        recipe_data = (title, "", 0, 0, "")
        self.cursor.execute(self.queries["AddRecipe"], recipe_data)
        self.db_connection.commit()
        print(f"{self.cursor.rowcount} row added.")
        
    def get_last_inserted_recipe_id(self) -> int:
        """
        Retrieves the ID of the last inserted recipe.

        Returns:
            int: The ID of the last inserted recipe.
        """
        self.cursor.execute("SELECT LAST_INSERT_ID();")
        last_inserted_id = self.cursor.fetchall()
        return last_inserted_id[0][0]
        
    def delete_recipe_by_id(self, id: int):
        """
        Deletes a recipe from the database by its ID.

        Args:
            id: The ID of the recipe to delete.
        """
        self.cursor.execute(self.queries["DeleteRecipeById"], (id,))
        self.db_connection.commit()
        print(f"{self.cursor.rowcount} row deleted.")
        
    def update_recipe(self, id: int, title: str, description: str, prep_time: str, cook_time: str, instructions: str):
        """
        Updates a recipe in the database.

        Args:
            id: The ID of the recipe to update.
            title: The new title of the recipe.
            description: The new description of the recipe.
            prep_time: The new preparation time of the recipe.
            cook_time: The new cooking time of the recipe.
            instructions: The new instructions of the recipe.
        """
        recipe_data = (title, description, prep_time, cook_time, instructions, id)
        self.cursor.execute(self.queries["UpdateRecipe"], recipe_data)
        self.db_connection.commit()
        print(f"{self.cursor.rowcount} row updated.")