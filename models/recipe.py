class Recipe():
    def __init__(self, id = None, recept = None, ingredients = None):
        self.id = id
        self.recept = recept
        self.ingredients = ingredients

    @classmethod
    def from_dict(cls, data):
        return Recipe(**data)

        

