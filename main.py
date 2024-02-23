# main.py
import tkinter as tk
from views.custom_window import AppWindow
from db.db_login import HOST, USER, PASSWORD, DATABASE
import mysql.connector

if __name__ == "__main__":
    # Create an instance of the app and run it
    app = AppWindow("My App", 1280, 720, False)
    
    # Connect to the database
    db_connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    # cursor = db_connection.cursor()
    # cursor.execute("select * from recipes")
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)
    
    # Run the tkinter window mainloop
    app.mainloop()