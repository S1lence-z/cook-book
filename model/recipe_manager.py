import mysql.connector
from .recipe import Recipe

class RecipeManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.cursor = db_connection.cursor()
        self.queries = {
            "GetAllRecipes": "SELECT * FROM recipes"
        }
        
    def list_all_recipes(self) -> list[Recipe]:
        all_recipes = []
        self.cursor.execute(self.queries["GetAllRecipes"])
        all_recipes_raw = self.cursor.fetchall()
        for recipe in all_recipes_raw:
            id = recipe[0]
            title = recipe[1]
            description = recipe[2]
            prep_time = recipe[3]
            cook_time = recipe[4]
            instructions = recipe[5]
            all_recipes.append(Recipe(id, title, description, prep_time, cook_time, instructions))
        return all_recipes
            
    def delete_recipe_by_name(self, name: str):
        return