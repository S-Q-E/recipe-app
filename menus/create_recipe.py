from menus.base_menu import BaseMenu
from utils import * 
from exceptions import *
from utils_for_db import *
import json
from models.recipe import Recipe

class CreateRecipe(BaseMenu):
    header = "****Creating pecipe*****"
    
    def show(self):
        name_of_recipe = input("Enter name of recipe")

        items = select_ingredients()
        products = []
        for i in items:
            products.append(i['ingredient'])
            
        recipe_ingredient = []
        max_ingredients = count_ingrediets()
        
        while len(products) <= max_ingredients['items']:
            for i in items:
                print(i['id'], i['ingredient'])

            add_ingred = input("Enter ingrediente (# stop): ")
            if add_ingred == '#':
                break
            if add_ingred not in products:
                print("Not such ingredients, try again!")
                continue
            else:
                recipe_ingredient.append(add_ingred)
            print(recipe_ingredient)
        
        recipe = Recipe(id = None, recept = name_of_recipe, ingredients = json.dumps(recipe_ingredient))
        result = insert_recipe(recipe)
        input('Recipe created! Press Enter...')


            
