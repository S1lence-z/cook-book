CREATE database cookBook;

CREATE TABLE IF NOT EXISTS recipes (
    recipe_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL UNIQUE,
    _description TEXT,
    prep_time INTEGER NOT NULL DEFAULT 0,
    cook_time INTEGER NOT NULL DEFAULT 0,
    instructions TEXT
);

INSERT INTO recipes (title, _description, prep_time, cook_time, instructions)
VALUES
('Spaghetti Carbonara', 'Classic Italian pasta dish with eggs, cheese, pancetta, and pepper', 15, 20, 'Cook pasta, fry pancetta, mix with beaten eggs and cheese, combine with pasta, season with pepper.'),
('Penne Arrabbiata', 'Spicy tomato-based sauce with garlic and red chili peppers', 10, 25, 'Sauté garlic and chili, add tomato sauce, simmer, then toss with cooked penne.'),
('Fettuccine Alfredo', 'Creamy pasta dish with butter and Parmesan cheese', 10, 15, 'Cook fettuccine, mix with melted butter and Parmesan until creamy, serve immediately.'),
('Lasagna Bolognese', 'Layered pasta with Bolognese sauce, béchamel, and cheese', 30, 45, 'Prepare Bolognese and béchamel sauce, layer with lasagna noodles and cheese, bake until golden.'),
('Pesto Pasta', 'Pasta with a sauce of basil, garlic, pine nuts, Parmesan, and olive oil', 15, 10, 'Blend basil, garlic, pine nuts, Parmesan, and oil to make pesto, toss with cooked pasta.'),
('Caesar Salad', 'Classic salad with romaine lettuce, croutons, Parmesan cheese, and Caesar dressing', 20, 0, 'Toss romaine lettuce with croutons, Parmesan cheese, and Caesar dressing.'),
('Greek Salad', 'Refreshing salad with tomatoes, cucumber, red onion, feta cheese, and olives', 15, 0, 'Combine tomatoes, cucumber, red onion, feta cheese, and olives, dress with olive oil and vinegar.'),
('Quinoa Salad', 'Healthy salad with quinoa, mixed vegetables, and a lemon vinaigrette', 20, 15, 'Cook quinoa, let cool, then mix with vegetables and dress with lemon vinaigrette.'),
('Tiramisu', 'Popular Italian coffee-flavored dessert with layers of ladyfingers and mascarpone cheese', 30, 0, 'Layer coffee-soaked ladyfingers with a mixture of mascarpone cheese and sugar, dust with cocoa powder.'),
('Chocolate Mousse', 'Rich and creamy dessert made with chocolate, eggs, and whipped cream', 20, 0, 'Melt chocolate, mix with beaten eggs, fold in whipped cream, chill until set.');

SELECT * from recipes;

DROP TABLE recipes;