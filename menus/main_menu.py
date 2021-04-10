from utils import get_option_input, raise_exception
from menus.base_menu import BaseMenu
from menus.create_recipe import CreateRecipe
from menus.delete_recipe import DeleteRecipe
from menus.recipe_list import RecipeList

class MainMenu(BaseMenu):
    header = "******Main Menu******"
    options = '[1] - Create recipe\n[2] - Recipe list\n[3] - Delete recipe\n[4] - Exit'
    next_menus = {
        '1': CreateRecipe,
        '2': RecipeList,
        '3': DeleteRecipe,
        '4': lambda: raise_exception(KeyboardInterrupt)
    }


    def show(self):
        input_func = get_option_input()

        def get_input():
            selected_option = input_func('Enter option')
            if selected_option not in self.next_menus.keys():
                raise UserInputOptionException
            return selected_option

        while True:
            print(self.header)
            print(self.options)

            selected_option = self.input_secure_wrap(get_input)

            next_menu = self.next_menus[selected_option]()
            
            next_menu.show()
            


     