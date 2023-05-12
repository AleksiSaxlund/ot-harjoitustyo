# Arkkitehtuuri

## Sovelluksen rakenne

### Koodin pakkausrakenne

```mermaid

classDiagram
    class ui
    class services
    class repositories
    class entities

    ui --> services
    services --> entities
    services --> repositories
    repositories --> entities

```

Hakemisto *ui* vastaa käyttöliittymästä, *services* hoitaa sovelluslogiikan sekä laskennan, *repositories* kommunikoi tietokantojen kanssa ja *entities* hakemistossa määritellään luokkia, jotka esittävät ainesosia ja reseptiä.

### Luokkarakenne

```mermaid

classDiagram
    class ui
    class malts_scrollarea
    class hops_scrollarea
    class yeasts_scrollarea
    class calculations_grid
    class manager_services
    class calculations_services
    class recipe
    class all_ingredients
    class ingredients_repository
    class notes_text_box

    ui "1" -- "1" malts_scrollarea
    ui "1" -- "1" hops_scrollarea
    ui "1" -- "1" yeasts_scrollarea
    ui "1" -- "1" calculations_grid
    ui "1" -- "1" notes_text_box
    malts_scrollarea -- manager_services
    hops_scrollarea -- manager_services
    yeasts_scrollarea -- manager_services
    calculations_grid -- manager_services
    manager_services "1" -- "1" recipe
    manager_services -- calculations_services
    manager_services -- ingredients_repository
    recipe "1" -- "1" calculations_services
    ingredients_repository "1" -- "*" all_ingredients
    calculations_services ..> all_ingredients
    manager_services ..> all_ingredients

```
## Tietokannat

Sovelluksella on kolme tietokantaan, jokaiselle pääainesosalle (Maltaat, humalat ja hiivat). Jokaiselle tietokannalle on oma repository-luokka, joka vastaa tiedon hakemisesta tietokannoista. Tulevaisuudessa näihin luokkiin voidaan lisätä ominaisuudet tiedon lisäämiselle ja poistamiselle tietokannoista.

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

### Reseptin koon muuttaminen

```mermaid

sequenceDiagram
    actor user
    participant ui
    participant manager_services
    participant calculations_services
    participant recipe

    user ->> ui: Change volume from the line edit
    activate ui
    ui ->> manager_services: volume_changed(new_volume)
    activate manager_services
    manager_services ->> recipe: recipe.volume = new_volume
    activate recipe
    recipe -->> manager_services:  none
    deactivate recipe
    manager_services ->> manager_services: update_calculations()
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

### Muut toiminnallisuudet

Kuten kahdesta aikaisemmasta kaaviosta huomaa, useat sovelluksessa tehtävät muutokset reseptiin noudattavat pitkälti samaa kaavaa. Aine valitaan ja lisätään reseptiin, jonka jälkeen suoritetaan laskut uudestaan ja päivitetään uudet tiedot näkyviin käyttäjälle.
