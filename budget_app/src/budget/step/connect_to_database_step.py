from mssql_python import connect
from budget.store import Store


class ConnectToDatabaseStep:
    def run(self) -> None:
        Store.cursor = connect(Store.connection_string).cursor()
