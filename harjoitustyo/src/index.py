from repositories.malts_repository import MaltsRepository
import database_connections
from services.calculations_services import CalculationsService
from entities.recipe import Recipe
from entities.all_ingredients import Malt

def temp_main_loop():
    recipe = Recipe()
    calculator = CalculationsService(recipe)
    all_malts = MaltsRepository(database_connections.get_malts_connection())

    while True:
        print("1: Add malt to the recipe")
        print("2: Change recipe volume")
        print("3: Calculate Original Gravity")
        print("4: Calculate SRM color")
        print("5: Search malts from the database")
        print("6: End")
        print()

        action = input("Action: ")

        if action == "1":
            print()
            amount = int(input("Amount "))
            name = input("Name: ")
            ppg = float(input("Points per Pound per Gallon: "))
            srm = int(input("SRM color: "))

            malt = Malt(name, ppg, srm)
            malt.amount = amount

            recipe.malts.append(malt)

        elif action == "2":
            print()
            volume = float(input("Volume of the recipe: "))
            recipe.volume = volume

        elif action == "3":
            if recipe.volume > 0:
                result = calculator.calculate_original_gravity()
                print("Original Gravity", result)
            else:
                print("The volume of the recipe must be greater than 0")

        elif action == "4":
            if recipe.volume > 0:
                result = calculator.calculate_color()
                print("SRM color", result)
            else:
                print("The volume of the recipe must be greater than 0")

        elif action == "5":
            print("The result format will be: [('Name', 'ppg', 'srm')]")
            search = input("Search by name: ")
            print(all_malts.find_malt(search))
            print()
            print("Currently the malt data must be manually written into the recipe.")

        elif action == "6":
            break
        print()
        action = input("Continue? y/n: ")
        if action == "n":
            break
        else:
            continue


temp_main_loop()