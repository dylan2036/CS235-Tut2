class Recipe:
    def __init__(self, id, name, images, author, date, description, ingredients, rating,
                 ingredient_quantities, preparation_time, instructions, category,
                 cook_time, recipe_yield, servings, reviews):

        self._id = id
        self._name = name
        self._images = images
        self._author = author
        self._date = date
        self._description = description
        self._ingredients = ingredients
        self._rating = rating
        self._ingredient_quantities = ingredient_quantities
        self._preparation_time = preparation_time
        self._instructions = instructions
        self._category = category
        self._cook_time = cook_time
        self._recipe_yield = recipe_yield
        self._servings = servings
        self._reviews = reviews


    def __str__(self):
        return f"<Recipe {self._name} with id: {self._id} was created by {self._author} on {self._date}>"
