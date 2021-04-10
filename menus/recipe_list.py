from menus.base_menu import BaseMenu
from utils import raise_exception, get_option_input
from exceptions import ExitFromMenuException
from utils_for_db import select_all_recipes
import json
class RecipeList(BaseMenu):
    header = "*****Recipe List*****"
    options = "[1] Exit"
    next_menus = {'1': lambda *_: raise_exception(ExitFromMenuException)}

    def show(self):
        print(self.header)

        recipes = select_all_recipes()

        for i in recipes:
            recipe = i['recept']
            ingredients = i['ingredients']
            print(f"Name: {recipe}\nIngredients: {ingredients}")

        input("Press Enter to exit")