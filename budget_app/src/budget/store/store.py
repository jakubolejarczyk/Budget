from budget.util import EnvUtil


class Store:
    server: str
    database: str
    encrypt: str
    trusted_connection: str
    trust_server_certificate: str

    @staticmethod
    def init() -> None:
        Store.server = EnvUtil.get_env("SERVER")
        Store.database = EnvUtil.get_env("DATABASE")
        Store.encrypt = EnvUtil.get_env("ENCRYPT")
        Store.trusted_connection = EnvUtil.get_env("TRUSTED_CONNECTION")
        Store.trust_server_certificate = EnvUtil.get_env(
            "TRUST_SERVER_CERTIFICATE"
        )

    @staticmethod
    def terminate() -> None:
        Store.server = None
        Store.database = None
        Store.encrypt = None
        Store.trusted_connection = None
        Store.trust_server_certificate = None
