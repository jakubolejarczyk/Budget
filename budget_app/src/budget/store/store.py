class Store:
    server: str
    database: str
    encrypt: str
    trusted_connection: str
    trust_server_certificate: str

    @staticmethod
    def init() -> None:
        Store.server = None
        Store.database = None
        Store.encrypt = None
        Store.trusted_connection = None
        Store.trust_server_certificate = None

    @staticmethod
    def terminate() -> None:
        Store.server = None
        Store.database = None
        Store.encrypt = None
        Store.trusted_connection = None
        Store.trust_server_certificate = None
