# main.py
from db.db_login import HOST, USER, PASSWORD, DATABASE
import mysql.connector
from views.custom_window import AppWindow
from .cook_book_app import CookBookApp
from .model.recipe_manager import RecipeManager

if __name__ == "__main__":
    # Connect to the database
    db_connection = mysql.connector.connect(
        host = HOST,
        user = USER,
        password = PASSWORD,
        database = DATABASE
    )
    # Create the model
    recipe_manager = RecipeManager(db_connection)
    # Create an instance of the app and run it
    main_window = AppWindow("My App", 1280, 720, False)
    app = CookBookApp(main_window, recipe_manager)
    # Run the tkinter window mainloop
    app.window.mainloop()
    
    #? Close the database connection? When?