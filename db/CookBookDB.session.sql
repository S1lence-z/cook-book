CREATE database cookBook;

CREATE TABLE IF NOT EXISTS recipes (
    recipe_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    prep_time INT NOT NULL DEFAULT 0,
    cook_time INT NOT NULL DEFAULT 0,
    instructions TEXT NOT NULL,
    category ENUM('Main Course', 'Dessert', 'Appetizer', 'Salad', 'Beverage', 'Snack', 'Vegetarian', 'Vegan', 'None') DEFAULT 'None'
);

SELECT * from recipes;

DROP TABLE recipes;

INSERT INTO recipes (title, description, prep_time, cook_time, instructions, category)
VALUES
('Spaghetti Carbonara', 'Classic Italian pasta dish with eggs, cheese, pancetta, and pepper', 15, 20, 'Cook pasta, fry pancetta, mix with beaten eggs and cheese, combine with pasta, season with pepper.', 'Main Course'),
('Penne Arrabbiata', 'Spicy tomato-based sauce with garlic and red chili peppers', 10, 25, 'Sauté garlic and chili, add tomato sauce, simmer, then toss with cooked penne.', 'Main Course'),
('Fettuccine Alfredo', 'Creamy pasta dish with butter and Parmesan cheese', 10, 15, 'Cook fettuccine, mix with melted butter and Parmesan until creamy, serve immediately.', 'Main Course'),
('Lasagna Bolognese', 'Layered pasta with Bolognese sauce, béchamel, and cheese', 30, 45, 'Prepare Bolognese and béchamel sauce, layer with lasagna noodles and cheese, bake until golden.', 'Main Course'),
('Pesto Pasta', 'Pasta with a sauce of basil, garlic, pine nuts, Parmesan, and olive oil', 15, 10, 'Blend basil, garlic, pine nuts, Parmesan, and oil to make pesto, toss with cooked pasta.', 'Main Course'),
('Caesar Salad', 'Classic salad with romaine lettuce, croutons, Parmesan cheese, and Caesar dressing', 20, 0, 'Toss romaine lettuce with croutons, Parmesan cheese, and Caesar dressing.', 'Salad'),
('Greek Salad', 'Refreshing salad with tomatoes, cucumber, red onion, feta cheese, and olives', 15, 0, 'Combine tomatoes, cucumber, red onion, feta cheese, and olives, dress with olive oil and vinegar.', 'Salad'),
('Quinoa Salad', 'Healthy salad with quinoa, mixed vegetables, and a lemon vinaigrette', 20, 15, 'Cook quinoa, let cool, then mix with vegetables and dress with lemon vinaigrette.', 'Salad'),
('Tiramisu', 'Popular Italian coffee-flavored dessert with layers of ladyfingers and mascarpone cheese', 30, 0, 'Layer coffee-soaked ladyfingers with a mixture of mascarpone cheese and sugar, dust with cocoa powder.', 'Dessert'),
('Chocolate Mousse', 'Rich and creamy dessert made with chocolate, eggs, and whipped cream', 20, 0, 'Melt chocolate, mix with beaten eggs, fold in whipped cream, chill until set.', 'Dessert');

CREATE TABLE IF NOT EXISTS ingredients (
    ingredient_id INT PRIMARY KEY AUTO_INCREMENT,
    recipe_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    quantity VARCHAR(255) NOT NULL,
    calories INT NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id) ON DELETE CASCADE
);

-- Inserting two key ingredients for each recipe assuming recipe_id from 1 to 10
INSERT INTO ingredients (recipe_id, name, quantity, calories) VALUES
(1, 'Pancetta', '100g', 500), -- Spaghetti Carbonara
(1, 'Eggs', '2', 140), -- Spaghetti Carbonara
(2, 'Penne pasta', '200g', 350), -- Penne Arrabbiata
(2, 'Tomato sauce', '400g', 160), -- Penne Arrabbiata
(3, 'Fettuccine pasta', '200g', 350), -- Fettuccine Alfredo
(3, 'Parmesan cheese', '100g', 431), -- Fettuccine Alfredo
(4, 'Lasagna noodles', '12 sheets', 774), -- Lasagna Bolognese
(4, 'Béchamel sauce', '200g', 300), -- Lasagna Bolognese
(5, 'Pasta', '200g', 350), -- Pesto Pasta
(5, 'Pine nuts', '30g', 179), -- Pesto Pasta
(6, 'Romaine lettuce', '1 head', 106), -- Caesar Salad
(6, 'Caesar dressing', '100ml', 780), -- Caesar Salad
(7, 'Tomatoes', '3', 60), -- Greek Salad
(7, 'Cucumber', '1', 16), -- Greek Salad
(8, 'Quinoa', '200g', 222), -- Quinoa Salad
(8, 'Lemon juice', '3 tablespoons', 12), -- Quinoa Salad
(9, 'Ladyfingers', '24', 480), -- Tiramisu
(9, 'Coffee', '1 cup', 2), -- Tiramisu
(10, 'Chocolate', '200g', 1200), -- Chocolate Mousse
(10, 'Eggs', '4', 280); -- Chocolate Mousse

SELECT * from ingredients;