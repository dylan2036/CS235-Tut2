from recipe import Recipe
from category import Category
from datetime import datetime

recipe1 = Recipe(
    id=1,
    name="Spaghetti Carbonara",
    images=["carbonara.jpg"],
    author="Chef Mario",
    date=datetime(2025, 8, 5),
    description="Classic Italian pasta dish.",
    ingredients=["spaghetti", "eggs", "cheese", "pancetta"],
    rating=4.8,
    ingredient_quantities=["200g", "2", "50g", "100g"],
    preparation_time="10 minutes",
    instructions=["Boil pasta", "Cook pancetta", "Mix eggs and cheese", "Combine everything"],
    category=[],
    cook_time="15 minutes",
    recipe_yield="2 servings",
    servings=2,
    reviews=["Amazing!", "Restaurant quality."]
)

cat1 = Category(101, "Italian")
cat2 = Category(132, "Pasta")

cat1.add_recipe(recipe1)
cat2.add_recipe(recipe1)

print("Recipes:")
print(recipe1)

print("\nCategories:")
print(cat1)
print(cat2)

print("\nCategory contents:")
print(cat1.list_recipes())
print(cat2.list_recipes())
