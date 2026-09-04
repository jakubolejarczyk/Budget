from budget.store import Store


class TerminateStoreStep:
    def run(self) -> None:
        Store.server = None
        Store.database = None
        Store.encrypt = None
        Store.trusted_connection = None
        Store.trust_server_certificate = None
        Store.connection_string = None
        Store.cursor = None
        Store.is_running = False
