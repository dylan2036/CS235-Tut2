class Recipe:
    def __init__(self, name, images, ingredients, author, date, rating, ingredient_quantities,
                 preparation_time, instructions, category, id, cook_time, recipe_yield, servings,
                 description, reviews):

        self._id = id
        self._name = name
        self._images = images
        self._ingredients = ingredients
        self._author = author
        self._date = date
        self._rating = rating
        self._ingredient_quantities = ingredient_quantities
        self._preparation_time = preparation_time
        self._instructions = instructions
        self._category = category
        self._cook_time = cook_time
        self._recipe_yield = recipe_yield
        self._servings = servings
        self._description = description
        self._reviews = reviews
