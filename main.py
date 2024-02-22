# main.py
import tkinter as tk
from custom_window import AppWindow

if __name__ == "__main__":
    app = AppWindow("My App", 1280, 720, False)
    app.mainloop()