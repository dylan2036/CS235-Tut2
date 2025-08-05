class Category:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__recipes = []

    def add_recipe(self, recipe):
        if recipe not in self.__recipes:
            self.__recipes.append(recipe)
            if hasattr(recipe, "add_category"):
                recipe.add_category(self)

    def __str__(self):
        return f"<Category {self.__id}: {self.__name}>"

    def list_recipes(self):
        recipe_strings = [str(recipe) for recipe in self.__recipes]
        return f"Category {self.__name} has the following associated recipes: [{', '.join(recipe_strings)}]"
