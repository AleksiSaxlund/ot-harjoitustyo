
class MaltsRepository:

    def __init__(self, connection):
        self._connection = connection

    def find_malt(self, search: str):
        connection = self._connection

        found = connection.execute("SELECT name, ppg, color FROM Malts WHERE name LIKE ?", [f'%{search}%']).fetchall()

        return found
    