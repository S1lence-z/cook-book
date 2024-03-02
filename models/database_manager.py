import mysql.connector
from models.recipe import Recipe

class DatabaseManager:
    def __init__(self, db_connection):
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
        all_recipes = []
        self.cursor.execute(self.queries["GetAllRecipes"])
        all_recipes_raw = self.cursor.fetchall()
        for recipe in all_recipes_raw:
            id, title, description, prep_time, cook_time, instructions = recipe
            all_recipes.append(Recipe(id, title, description, prep_time, cook_time, instructions))
        return all_recipes
    
    def get_recipe_by_id(self, id: int) -> Recipe:
        self.cursor.execute(self.queries["GetRecipeById"], (id,))
        recipe = self.cursor.fetchall()
        id, title, description, prep_time, cook_time, instructions = recipe[0]
        return Recipe(id, title, description, prep_time, cook_time, instructions)
            
    def add_recipe(self, title: str, description: str, prep_time: str, cook_time: str, instructions: str):
        recipe_data = (title, description, prep_time, cook_time, instructions)
        self.cursor.execute(self.queries["AddRecipe"], recipe_data)
        self.db_connection.commit()
        print(f"{self.cursor.rowcount} row added.")
        
    def delete_recipe_by_id(self, id: int):
        self.cursor.execute(self.queries["DeleteRecipeById"], (id,))
        self.db_connection.commit()
        print(f"{self.cursor.rowcount} row deleted.")
        
    def update_recipe(self, id: int, title: str, description: str, prep_time: str, cook_time: str, instructions: str):
        recipe_data = (title, description, prep_time, cook_time, instructions, id)
        self.cursor.execute(self.queries["UpdateRecipe"], recipe_data)
        self.db_connection.commit()
        print(f"{self.cursor.rowcount} row updated.")