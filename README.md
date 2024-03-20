# CookBook

## Description
This is a simple recipe manager app. You can add your custom recipes along with their ingredients and then you can generate a PDF file containing all the ingredients, so you can easily keep track of you recipes and their preparation process.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites
Before running the CookBook application, ensure you have the following libraries installed:

- **Tkinter**: A standard GUI library for Python.
- **customtkinter**: A library to create modern and customizable GUIs based on Tkinter.
- **MySQL Connector/Python (mysql-connector-python)**: A library to connect your application to a MySQL database.

### Download necessary libraries
To install these libraries, use the following commands:

1. Tkinter (usually comes pre-installed with Python, but in case it's not):
   ```
   pip install tkinter
   ```

2. Customtkinter:
    ```
    pip install customtkinter
    ```

3. MySQL connector for Python:
    ```
    pip install mysql-connector-python
    ```

Ensure these installations are successful before proceeding to the installation of the CookBook application.

## Installation
### To download the repository, follow these steps:

1. Clone this repository to your local machine
   ```
   git clone https://github.com/S1lence-z/cook-book.git
   ```

2. Go to the downloaded directory in the folder from which you start the command above

### To start the program, follow either these steps:

1. Open the cloned directory in your favorite IDE

2. Open the db folder and create the database and two tables as in the file: CookBookDB.session.sql. You can also populate it with the testing data

3. Change your login credentials in the db_login.py file to your local databse

4. Alternatively, you can navigate to the cloned directory in your command line and run the following command:
    ```
    python main.py
    ```

## Usage
### Recipes page:
This page shows a list of all the recipes. You can view, edit, or delete a recipe from this page.

[Recipes page](./docs/recipes_page.png)

### Edit recipe page:
This page allows you to edit the details of a specific recipe. You can modify the recipe name, ingredients, and instructions.

[Edit recipe page](./docs/edit_recipe_page.png)

### Recipe detail page:
This page displays the detailed information of a specific recipe. It includes the recipe name, ingredients, instructions, and an image of the dish.

[Recipe detail page](./docs/recipe_detail_page.png)

### Ingredients page:
This page lists all the ingredients used in the recipes. You can add, edit, or delete ingredients from this page.

[Ingredients page](./docs/ingredients_page.png)

### Generate PDF window:
This window allows you to generate a PDF file containing all the ingredients of your recipes. It helps you keep track of the ingredients needed for your recipes.

[Generate PDF window](./docs/generate_pdf_window.png)

## Contributing
Explain how others can contribute to your project. Include guidelines for submitting pull requests or reporting issues.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Contact
If you have any questions or suggestions please contact me on this email address:
j3.zelenka@gmail.com

## Additional Documents
[Used Python Naming Conventions](./docs/python_naming_conventions.md)
