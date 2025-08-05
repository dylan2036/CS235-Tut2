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

recipe1 = Recipe(
    id=1,
    name="Spaghetti Carbonara",
    images=["carbonara1.jpg", "carbonara2.jpg"],
    author="Chef Mario",
    date="2025-08-05",
    description="A classic Italian pasta dish made with eggs, cheese, pancetta, and pepper.",
    ingredients=["spaghetti", "eggs", "parmesan cheese", "pancetta", "black pepper", "salt"],
    rating=4.7,
    ingredient_quantities=["200g", "2", "50g", "100g", "to taste", "to taste"],
    preparation_time="10 minutes",
    instructions=[
        "1: Boil pasta until al dente.",
        "2: Cook pancetta until crispy.",
        "3: Mix eggs and cheese in a bowl.",
        "4: Combine all ingredients with pasta off the heat.",
        "5: Serve immediately with extra cheese and pepper."
    ],
    category="Pasta",
    cook_time="15 minutes",
    recipe_yield="2 servings",
    servings=2,
    reviews=["Delicious and creamy!", "Easy and authentic!", "My go-to pasta recipe."]
)
