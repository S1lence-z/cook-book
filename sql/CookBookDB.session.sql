CREATE TABLE IF NOT EXISTS recipes (
    recipe_id INTEGER PRIMARY KEY auto_increment,
    title TEXT not null,
    _description TEXT,
    prep_time INTEGER not null,
    cook_time INTEGER not null,
    instructions TEXT
);

INSERT INTO recipes (title, _description, prep_time, cook_time, instructions)
VALUES
('Classic Spaghetti Carbonara', 'A quick and easy Italian pasta dish using eggs, cheese, and bacon.', 15, 20, 'Cook pasta. Fry bacon. Mix eggs and cheese. Combine all with pasta.'),
('Homemade Margherita Pizza', 'Simple pizza with tomatoes, mozzarella cheese, and fresh basil.', 20, 15, 'Prepare dough. Add toppings. Bake until crust is golden.'),
('Vegetarian Chili', 'Hearty and spicy chili made with beans, tomatoes, and various vegetables.', 25, 35, 'Saute vegetables. Add tomatoes and beans. Simmer.'),
('Banana Bread', 'Moist and delicious bread made with overripe bananas, flour, sugar, and eggs.', 15, 60, 'Mix ingredients. Pour into loaf pan. Bake.'),
('Chicken Caesar Salad', 'Classic Caesar salad with grilled chicken, romaine lettuce, croutons, and Caesar dressing.', 20, 10, 'Grill chicken. Toss lettuce with dressing and croutons. Top with chicken.');

SELECT * from recipes;