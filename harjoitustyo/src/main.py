from repositories.malts_repository import MaltsRepository
import database_connections
from services.calculations_services import CalculationsService
from entities.recipe import Recipe
from entities.all_ingredients import Malt

q = Recipe()
q.malts = []
q.volume = 4
#q.malts[0].amount = 4
asd = CalculationsService(q)

print(asd.calculate_color())