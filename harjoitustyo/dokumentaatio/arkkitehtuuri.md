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