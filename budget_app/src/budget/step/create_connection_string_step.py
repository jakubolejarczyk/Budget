from budget.store import Store


class CreateConnectionStringStep:
    def run(self) -> None:
        Store.connection_string = f"Server={Store.server};Database={Store.database};Encrypt={Store.encrypt};Trusted_Connection={Store.trusted_connection};TrustServerCertificate={Store.trust_server_certificate};"
