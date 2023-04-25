#Arkkitehtuuri

## Alustava rakenne
Päivitetään, kun GUI otetaan käyttöön.

```mermaid

classDiagram
    class management_services
    class calculations_services
    class recipe
    class all_ingredients
    class ingredients_repository

    management_services "1" -- "1" recipe
    management_services -- calculations_services
    management_services -- ingredients_repository
    recipe "1" -- "1" calculations_services
    ingredients_repository "1" -- "*" all_ingredients
    calculations_services ..> all_ingredients
    management_services ..> all_ingredients

```

## Toiminnallisuutta
Sovelluksen perustoiminnallisuuksia kuvattuna sekvenssikaavioina.

### Ainesosan (hiivan) lisääminen reseptiin GUI:n kautta

```mermaid

sequenceDiagram
    actor user
    participant ui
    participant manager_services
    participant calculations_services
    participant recipe

    user ->> ui: Select yeast from combobox
    activate ui
    ui ->> manager_services: ingredient_added(chosen_yeast, "yeasts")
    activate manager_services
    manager_services ->> recipe: ingredients["yeasts"].append(yeast)
    activate recipe
    recipe -->> manager_services: none
    deactivate recipe
    manager_services ->> manager_services: update_calculation()
    manager_services ->> calculations_services: get_all_calculations()
    activate calculations_services
    calculations_services ->> calculations_services: *calls calculation functions for all values
    calculations_services ->> recipe: 
    activate recipe
    recipe -->> calculations_services: *required ingredient data
    deactivate recipe
    calculations_services -->> manager_services: return results
    deactivate calculations_services
    manager_services ->> manager_services: format_calculation_results()
    manager_services ->> ui: return results
    deactivate manager_services
    ui ->> ui: data_grid.update_values(results)
    deactivate ui

```
*:lla merkatut: get_all_calculations funktio suorittaa kaikki muut calculations_servicesissä määritellyt funktiot ja palauttaa niiden tulokset. Jokainen näistä funktioista hakee recipe-oliosta tarvittavat tiedot.