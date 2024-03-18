from custom.ingredient import Ingredient

class IngredientsTable:
    def __init__(self) -> None:
        """
        Initializes an instance of IngredientsTable.
        """
        self._table = []
        
    def populate(self, header: list, ingredients: list[Ingredient], final_row: bool) -> None:
        """
        Populates the ingredients table with header, ingredients, and an optional final row.

        Args:
            header (list): The header row of the table.
            ingredients (list[Ingredient]): The list of Ingredient objects.
            final_row (bool): Whether to add a final row with total calories.

        Returns:
            None
        """
        self._table.append(header)
        for ing in ingredients:
            self._table.append([str(ing.name), str(ing.quantity), str(ing.calories)])
        if final_row:
            self._add_final_row()
    
    def get_table(self) -> list:
        """
        Returns the ingredients table.

        Returns:
            list: The ingredients table.
        """
        return self._table
    
    def clear_table(self) -> None:
        """
        Clears the ingredients table.

        Returns:
            None
        """
        self._table.clear()
        
    def _add_final_row(self) -> None:
        """
        Adds a final row to the ingredients table with the total calories.

        Returns:
            None
        """
        total_calories = sum(int(row[2]) for row in self._table[1:])
        self._table.append(["", "", ""])
        self._table.append(["", "Total", str(total_calories)])
