# main.py
import tkinter as tk
from custom_window import AppWindow
from db_login import HOST, USER, PASSWORD, DATABASE
import mysql.connector

if __name__ == "__main__":
    # app = AppWindow("My App", 1280, 720, False)
    # app.mainloop()
    
    db_connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )
    
    cursor = db_connection.cursor()
    cursor.execute("select * from recipes")
    rows = cursor.fetchall()
    for row in rows:
        print(row)