from enum import Enum

class RecipeCategory(Enum):
    MAIN_COURSE = 'Main Course'
    DESSERT = 'Dessert'
    APPETIZER = 'Appetizer'
    SALAD = 'Salad'
    BEVERAGE = 'Beverage'
    SNACK = 'Snack'
    VEGETARIAN = 'Vegetarian'
    VEGAN = 'Vegan'
    NONE = 'None'

    @classmethod
    def get_recipe_category(cls, value: str) -> 'RecipeCategory':
        """
        Returns the RecipeCategory enum value from a string value.
        
        Args:
            value: The string value of the RecipeCategory.
            
        Returns:
            RecipeCategory: The RecipeCategory enum value.
        """
        for category in cls:
            if category.value.lower() == value.lower():
                return category
        return cls.NONE
    
    @classmethod
    def validate_recipe_category(cls, value: str):
        """
        Validates the string value of the RecipeCategory.
        
        Args:
            value: The string value of the RecipeCategory.
            
        Returns:
            bool: True if the value is a valid RecipeCategory, False otherwise.
        """
        for category in cls:
            if category.value.lower() == value.lower():
                return True
        return False