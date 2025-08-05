class Recipe:
    def init(self, id, name, author, description, ingredients_list,
                 prep_instructions, cook_time):

        self._id = id
        self._name = name
        self._author = author
        self._description = description
        self._ingredients_list = ingredients_list
        self._prep_instructions = prep_instructions
        self._cook_time = cook_time