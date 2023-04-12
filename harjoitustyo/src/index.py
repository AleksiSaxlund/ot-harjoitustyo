from repositories.ingredients_repository import MaltsRepository
import database_connections
from services.calculations_services import CalculationsService
from entities.recipe import Recipe
from entities.all_ingredients import Malt


def temp_main_loop():
    recipe = Recipe()
    calculator = CalculationsService(recipe)
    all_malts = MaltsRepository(database_connections.get_malts_connection())

    while True:
        controls()
        action = input("Action: ")

        if action == "1":
            recipe.ingredients["malts"].append(create_malt())

        elif action == "2":
            recipe.volume = float(input("Volume of the recipe: "))

        elif action == "3":
            print("Original Gravity", calculator.calculate_original_gravity())
        
        elif action == "4":
            print("Final Gravity: ", calculator.calculate_final_gravity())

        elif action == "5":
            print("SRM color", calculator.calculate_color())

        elif action == "6":
            find_malt(all_malts)

        elif action == "7":
            break


def controls():
    print()
    print("1: Add malt to the recipe")
    print("2: Change recipe volume")
    print("3: Calculate Original Gravity")
    print("4: Calculate SRM color")
    print("5: Search malts from the database")
    print("6: End")
    print()


def create_malt():
    amount = int(input("Amount "))
    name = input("Name: ")
    ppg = float(input("Points per Pound per Gallon: "))
    srm = int(input("SRM color: "))

    malt = Malt(name, ppg, srm)
    malt.amount = amount

    return malt


def find_malt(all_malts):
    print("The result format will be: [('Name', 'ppg', 'srm')]")
    search = input("Search by name: ")
    print([malt for malt in all_malts.malts if search.lower() in malt[0].lower()])
    print()
    print("Currently the malt data must be manually written into the recipe.")


temp_main_loop()
