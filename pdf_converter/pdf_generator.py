from reportlab.pdfgen import canvas
from custom import Ingredient
from views.main_view import MainView
from pdf_converter.ingredients_table import IngredientsTable
from tkinter import filedialog

class PdfGenerator:
    """
    A class that generates a PDF file containing an ingredients list for a recipe.
    
    Attributes:
        view (MainView): The main view object.
        _file_title (str): The title of the PDF file.
        _pdf_table (IngredientsTable): The table object for storing ingredients.
    """
    
    def __init__(self, view: MainView) -> None:
        """
        Initializes a PdfGenerator object.
        
        Args:
            view (MainView): The main view object.
        """
        self.view = view
        self._file_title: str = ""
        self._pdf_table = IngredientsTable()
        
    def _set_file_title(self, recipe_name: str) -> None:
        """
        Sets the file title for the PDF.
        
        Args:
            recipe_name (str): The name of the recipe.
        """
        self._file_title = f"Ingredients list for {recipe_name}"
    
    def _get_table_header(self) -> list:
        """
        Returns the header of the table.
        
        Returns:
            list: The table header.
        """
        return ["Name", "Quantity", "Calories"]

    def _draw_table(self, canvas: canvas.Canvas, data: list[list[str]], start_x: int, start_y: int) -> None:
        """
        Draws the table on the canvas.
        
        Args:
            canvas (canvas.Canvas): The canvas object.
            data (list[list[str]]): The data to be displayed in the table.
            start_x (int): The starting x-coordinate of the table.
            start_y (int): The starting y-coordinate of the table.
        """
        cell_width = 100
        cell_height = 20
        num_rows = len(data)
        num_cols = len(data[0]) if num_rows > 0 else 0
        
        table_font = "Helvetica-Bold"
        table_font_size = 12
        table_header_color = "#000000"
        table_data_color = "#0000FF"
        
        for row in range(num_rows):
            for col in range(num_cols):
                x = start_x + col * cell_width
                y = start_y - row * cell_height
                
                if row == 0:
                    canvas.setFont(table_font, table_font_size)
                    canvas.setFillColor(table_header_color)
                else:
                    canvas.setFont("Helvetica", table_font_size)
                    canvas.setFillColor(table_data_color)
                
                canvas.drawString(x + 5, y - cell_height + 5, data[row][col])
                
        canvas.setFont("Helvetica", 10)
        canvas.setFillColor("#000000")

    def generate_pdf(self, ingredients: list[Ingredient], recipe_title: str) -> None:
        """
        Generates a PDF file containing an ingredients list for a recipe.
        
        Args:
            ingredients (list[Ingredient]): The list of ingredients.
            recipe_title (str): The title of the recipe.
        """
        self._set_file_title(recipe_title)
        table_header = self._get_table_header()
        self._pdf_table.populate(table_header, ingredients, final_row=True)
        table_data = self._pdf_table.get_table()
            
        save_location = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
            title="Save as"
        )
        
        if not save_location:
            print("No location selected")
            return
        
        c = canvas.Canvas(save_location)
        
        c.setFont("Helvetica", 16)
        text_width = c.stringWidth(self._file_title, "Helvetica", 16)
        x = (c._pagesize[0] - text_width) / 2
        c.drawString(x, 800, self._file_title)
        
        self._draw_table(c, table_data, 50, 780)
        c.save()
        self._pdf_table.clear_table()