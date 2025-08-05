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

recipe2 = Recipe(
    id=2,
    name="Margherita Pizza",
    images=["pizza.jpg"],
    author="Chef Luigi",
    date=datetime(2025, 8, 5),
    description="Simple and delicious pizza with fresh ingredients.",
    ingredients=["pizza dough", "tomato sauce", "mozzarella", "basil"],
    rating=4.5,
    ingredient_quantities=["1 base", "100g", "150g", "a few leaves"],
    preparation_time="15 minutes",
    instructions=["Prepare dough", "Spread tomato sauce", "Add cheese and basil", "Bake"],
    category=[],
    cook_time="12 minutes",
    recipe_yield="1 pizza",
    servings=2,
    reviews=["Fresh and tasty!", "Perfect crust."]
)

recipe3 = Recipe(
    id=3,
    name="Pesto Pasta",
    images=["pesto.jpg"],
    author="Chef Gianna",
    date=datetime(2025, 8, 5),
    description="Aromatic basil pesto tossed with pasta.",
    ingredients=["pasta", "basil", "garlic", "pine nuts", "olive oil", "parmesan"],
    rating=4.7,
    ingredient_quantities=["200g", "1 bunch", "2 cloves", "30g", "50ml", "40g"],
    preparation_time="5 minutes",
    instructions=["Boil pasta", "Blend pesto ingredients", "Mix together"],
    category=[],
    cook_time="10 minutes",
    recipe_yield="2 servings",
    servings=2,
    reviews=["Super flavourful!", "Loved it!"]
)

cat1 = Category(101, "Italian")
cat2 = Category(132, "Pasta")

cat1.add_recipe(recipe1)
cat2.add_recipe(recipe1)

cat1.add_recipe(recipe2)

cat1.add_recipe(recipe3)
cat2.add_recipe(recipe3)

# Output
print("Recipes:")
print(recipe1)
print(recipe2)
print(recipe3)

print("\nCategories:")
print(cat1)
print(cat2)

print("\nCategory contents:")
print(cat1.list_recipes())
print(cat2.list_recipes())
