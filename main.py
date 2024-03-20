from db.db_login import HOST, USER, PASSWORD, DATABASE
from cook_book_app import CookBookApp
from models.database_manager import DatabaseManager
import mysql.connector

if __name__ == "__main__":
    """Main entry point of the program."""
    
    # Connect to the database
    db_connection = mysql.connector.connect(
        host = HOST,  # Database host
        user = USER,  # Database username
        password = PASSWORD,  # Database password
        database = DATABASE  # Database name
    )
    
    # Create an instance of the database manager
    recipe_manager = DatabaseManager(db_connection)
    
    # Create the CookBookApp
    app = CookBookApp(recipe_manager)
    
    # Start the app
    app.start_app()
    
    # Close the database connection after the app is closed
    db_connection.close()
    print("Database connection closed.")