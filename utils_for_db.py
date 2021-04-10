from connection import DBService
from models.ingredients import Ingredients
db = DBService()

def count_ingrediets():
    try:
        query  = "SELECT COUNT(id) AS items FROM ingredients WHERE true"
        db.execute(query)

        if db.cursor.rowcount == 1:
            return db.cursor.fetchone()
        else:
            return None
    except Exception as ex:
        print(ex)

def select_ingredients():
    try:
        query  = "SELECT * FROM ingredients WHERE true"
        db.execute(query)

        if db.cursor.rowcount > 0:
            return db.cursor.fetchall()
                
        else:
            return None
    except Exception as ex:
        print("Error is here", ex)

def insert_recipe(recipe):
    try:
        query = "INSERT INTO recepts (recept, ingredients) values ('{recept}', '{ingredients}')"
        query = query.format(
            recept = recipe.recept,
            ingredients = recipe.ingredients
        )
        db.execute(query)
        return True
    except Exception as ex:
        print(ex)
        return False


def select_all_recipes():
    try:
        query = "SELECT * FROM recepts"
        db.execute(query)
        if db.cursor.rowcount > 0:
            return db.cursor.fetchall()
        else:
            return None
    except Exception as ex:
        print(ex)

def delete_recipe_by_id(id):
    try:
        query = "DELETE FROM recepts where id = %d" % id
        db.execute(query)
        return True
    except Exception as ex:
        print(ex)
        return False  
