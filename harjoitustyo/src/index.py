from repositories.ingredients_repository import MaltsRepository, HopsRepository, YeastsRepository
from services.calculations_services import CalculationsService
from entities.recipe import Recipe
from entities.all_ingredients import Malt, Hop, Yeast


def temp_main_loop_2():
    recipe, calculator, all_malts, all_hops, all_yeasts = initialize()
    controls()

    while True:
        show_calculations(calculator)
        show_ingredients(recipe)
        action = get_inputs()

        if action == "1":
            add_malt(all_malts, recipe)
        elif action == "2":
            add_hop(all_hops, recipe)
        elif action == "3":
            add_yeast(all_yeasts, recipe)
        elif action == "4":
            recipe.volume = float(input("The new volume: "))
        elif action == "5":
            break
        else:
            controls()

def initialize():
    recipe = Recipe()
    calculator = CalculationsService(recipe)
    all_malts = MaltsRepository()
    all_hops = HopsRepository()
    all_yeasts = YeastsRepository()
    return recipe, calculator, all_malts, all_hops, all_yeasts

def show_calculations(calculator):
    original_gravity, final_gravity, abv, color = calculator.get_all_calculations()
    print(
        f"original gravity: {original_gravity}, final gravity: {final_gravity}"
        f", ABV: {abv}, SRM: {color}")
    print()


def show_ingredients(recipe):
    print("Malts: ")
    [print(f"{malt.name}, - {malt.amount} lb") for malt in recipe.ingredients["malts"]]
    print()
    print("Hops: ")
    [print(hop.name) for hop in recipe.ingredients["hops"]]
    print()
    print("Yeasts: ")
    [print(yeast.name) for yeast in recipe.ingredients["yeasts"]]
    print()


def get_inputs():
    action = input("Action: ")
    return action


def add_malt(all_malts, recipe):
    print("Search the malt by name.")
    search = input("Search: ")
    found = all_malts.search(search)

    for malt in found:
        print(f"ID: {malt[0]}, name: {malt[1].name}")
    print()
    print("Choose the ID of the malt which you want to add to the recipe.")

    choice = int(input("ID: "))
    if choice <= len(found):
        print("Choose the amount of the malt.")
        amount = float(input("Amount: "))
        selected_malt = found[choice][1]
        selected_malt.amount = amount
        recipe.ingredients["malts"].append(selected_malt)
    else:
        print("Incorrect ID. Malt not added")


def add_hop(all_hops, recipe):
    print("Search the hop by name.")
    search = input("Search: ")
    found = all_hops.search(search)

    for hop in found:
        print(f"ID: {hop[0]}, name: {hop[1].name}")
    print()
    print("Choose the ID of the hop which you want to add to the recipe.")

    choice = int(input("ID: "))
    if choice <= len(found):
        selected_hop = found[choice][1]
        recipe.ingredients["hops"].append(selected_hop)
    else:
        print("Incorrect ID. Hop not added.")


def add_yeast(all_yeasts, recipe):
    print("Search the Yeast by name.")
    search = input("Search: ")
    found = all_yeasts.search(search)

    for yeast in found:
        print(f"ID: {yeast[0]}, name: {yeast[1].name}")
    print()
    print("Choose the ID of the hop which you want to add to the recipe.")

    choice = int(input("ID: "))
    if choice < len(found):
        selected_yeast = found[choice][1]
        recipe.ingredients["yeasts"].append(selected_yeast)
    else:
        print("Incorrect ID. Yeast not added.")


def controls():
    print()
    print("1: Add malt to the recipe")
    print("2: Add hop to the recipe")
    print("3: Add yeast to the recipe")
    print("4: Change recipe volume")
    print("5: End")
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
