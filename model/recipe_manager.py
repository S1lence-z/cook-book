import mysql.connector
from recipe import Recipe

class RecipeManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.cursor = db_connection.cursor()
        
    def list_all_recipes(self) -> list[Recipe]:
        all_recipes = []
        self.cursor.execute("SELECT * FROM recipes")
        all_recipes_raw = self.cursor.fetchall()
        for recipe in all_recipes_raw:
            print(recipe)
        return all_recipes
            
    def delete_recipe_by_name(self, name: str):
        return