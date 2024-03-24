from cook_book_app import CookBookApp
from models.database_manager import DatabaseManager
import sqlite3

if __name__ == "__main__":
    """Main entry point of the program."""
    
    # Connect to the database
    db_connection = sqlite3.connect("./db/main.db")
    
    # Create an instance of the database manager
    recipe_manager = DatabaseManager(db_connection)
    
    # Create the CookBookApp
    app = CookBookApp(recipe_manager)
    
    # Start the app
    app.start_app()
    
    # Close the database connection after the app is closed
    db_connection.close()
    print("Database connection closed.")