from mssql_python import connect
from budget.store import BudgetStore


class ConnectionDatabase:
    def create_connection(self) -> None:
        connection_string = f"Server={BudgetStore.server};Database={BudgetStore.database};Encrypt={BudgetStore.encrypt};Trusted_Connection={BudgetStore.trusted_connection};TrustServerCertificate={BudgetStore.trust_server_certificate};"
        connection = connect(connection_string)
        BudgetStore.cursor = connection.cursor()
