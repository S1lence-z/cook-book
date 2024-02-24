import mysql.connector
from .recipe import Recipe

class RecipeManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.cursor = db_connection.cursor()
        self.queries = {
            "GetAllRecipes": "SELECT * FROM recipes",
            "DeleteRecipeById": "DELETE FROM recipes WHERE id = %s"
        }
        
    def get_all_recipes(self) -> list[Recipe]:
        all_recipes = []
        self.cursor.execute(self.queries["GetAllRecipes"])
        all_recipes_raw = self.cursor.fetchall()
        for recipe in all_recipes_raw:
            id, title, description, prep_time, cook_time, instructions = recipe
            all_recipes.append(Recipe(id, title, description, prep_time, cook_time, instructions))
        return all_recipes
            
    def delete_recipe_by_id(self, id: str):
        self.cursor.execute(self.queries["DeleteRecipeById"], id)
        self.cursor.commit()
        print(f"{self.cursor.rowcount} row(s) deleted.")