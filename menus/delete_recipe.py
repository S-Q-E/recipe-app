from menus.base_menu import BaseMenu
from utils import get_id_input, get_confirm_input
from utils_for_db import delete_recipe_by_id, select_all_recipes
class DeleteRecipe(BaseMenu):
    header = "*****Recipe delete menu*****"
    
    def show(self):
        recipes = select_all_recipes()
        ids = []
        
        for i in recipes:
            ids.append(i['id'])
            print(f"Recipe ID: {i['id']}\nRecipe: {i['recept']}\n")
    
        select_id = get_id_input()
        def get_id():
            return int(select_id("Select recipe id"))

        confirm_input_func = get_confirm_input()
        def confirm():
            return confirm_input_func("Are you sure? ('y' or 'n'): ")

        while True:
            selected_id = self.input_secure_wrap(get_id)     
            
            if selected_id in ids:
                conf = self.input_secure_wrap(confirm)
                delete_recipe_by_id(selected_id)
                input("Recipe deleted!")
                return
            else:
                print("Error! Not such ID")
                continue
                

        