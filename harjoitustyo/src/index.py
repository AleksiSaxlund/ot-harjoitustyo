from repositories.ingredients_repository import MaltsRepository
from services.calculations_services import CalculationsService
from entities.recipe import Recipe
from entities.all_ingredients import Malt, Hop, Yeast


def temp_main_loop_2():
    while True:
        recipe = Recipe()
        calculator = CalculationsService(recipe)
        all_malts = MaltsRepository()
        controls()
        show_calculations(calculator)
        action = get_inputs()

        if action == "1":
            add_malt()
        elif action == "2":
            pass
        elif action == "3":
            pass
        elif action == "4":
            recipe.volume = float(input("The new volume: "))
        elif action == "5":
            pass
        else:
            break


def show_calculations(calculator):
    original_gravity, final_gravity, abv, color = calculator.get_all_calculations()
    print(
        f"original gravity: {original_gravity}, final gravity: {final_gravity}, ABV: {abv}, SRM: {color}")
    print()


def get_inputs():
    action = input("Action: ")
    return action


def add_malt(malts, recipe):
    print("Search the malt by name.")
    search = input("Search: ")
    found = malts.search(search)

    for malt in found:
        print(f"id: {malt[0]}, name: {malt[1].name}")
    print()
    print("Choose the ID of the malt which you want to add to the recipe.")

    choice = int(input("ID: "))
    if choice <= len(found):
        selected_malt = found[choice][1]
        recipe.ingredients["malts"].append(selected_malt)
    else:
        print("Incorrect ID.")


def controls():
    print()
    print("1: Add malt to the recipe")
    print("2: Add hop to the recipe")
    print("3: Add yeast to the recipe")
    print("4: Change recipe volume")
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


temp_main_loop_2()
