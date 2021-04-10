class Ingredients():
    def __init__(
        self,
        id = None,
        ingredient = None,
        pieces = None,
        weight = None,
        recept_id = None
    ):

        self.id = id,
        self.ingredient = ingredient,
        self.pieces = pieces
        self.weight = weight
        self.recept_id = recept_id

    @classmethod
    def from_dict(cls, data):
        return Ingredients(**data)


    # def __str__(self):
    #     return f"ID:{id}\ningredient: {ingredient}\npieces:{pieces}\nWieght: {weight}".format()



        