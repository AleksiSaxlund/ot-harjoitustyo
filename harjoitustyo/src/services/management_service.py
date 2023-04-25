from repositories.ingredients_repository import MaltsRepository, HopsRepository, YeastsRepository
from services.calculations_services import CalculationsService
from entities.recipe import Recipe

#
# This entire file is temporary. It's only purpose is to enable the app to be ran
# on the terminal until GUI has been implemented.
#


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
            recipe.notes.append(notes_input())
        elif action == "6":
            break
        else:
            controls()


def notes_input():
    print("New notes:")
    note = input()
    return note


def initialize():
    recipe = Recipe()
    calculator = CalculationsService(recipe)
    all_malts = MaltsRepository()
    all_hops = HopsRepository()
    all_yeasts = YeastsRepository()
    return recipe, calculator, all_malts, all_hops, all_yeasts


def show_calculations(calculator):
    original_gravity, final_gravity, abv, color, ibu = calculator.get_all_calculations()
    print(
        f"original gravity: {original_gravity}, final gravity: {final_gravity}"
        f", ABV: {abv}, SRM: {color}, IBU: {ibu}")
    print()


def show_ingredients(recipe):
    print("Malts: ")
    for malt in recipe.ingredients["malts"]:
        print(f"{malt.name}, - {malt.amount} lb")
    print()

    print("Hops: ")
    for hop in recipe.ingredients["hops"]:
        print(f"{hop.name}, - {hop.amount}")
    print()

    print("Yeasts: ")
    for yeast in recipe.ingredients["yeasts"]:
        print(yeast.name)
    print()

    print("Notes:")
    for row in recipe.notes:
        print(row)
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
    amount = float(input("Amount: "))
    if choice <= len(found):
        selected_hop = found[choice][1]
        selected_hop.amount = amount
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
    print("5: Add notes")
    print("6: End")
    print()
