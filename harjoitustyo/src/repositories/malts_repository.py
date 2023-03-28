import sqlite3 as sql
#from entities.malt import Malt
import database_connections

class MaltsRepository:

    def _init__(self, connection):
        self._connection = connection

    def find_malt(self, search: str):
        db = self._connection

        found = db.execute("SELECT * FROM Malts WHERE nimi LIKE %?%", [search]).fetch_all()

        return found
    
asd = MaltsRepository(database_connections.get_malts_connection())
print(asd.find_malt("pale"))