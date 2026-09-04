from budget.store import Store
from budget.util import EnvUtil


class InitStoreStep:
    def run(self) -> None:
        Store.server = EnvUtil.get_env("SERVER")
        Store.database = EnvUtil.get_env("DATABASE")
        Store.encrypt = EnvUtil.get_env("ENCRYPT")
        Store.trusted_connection = EnvUtil.get_env("TRUSTED_CONNECTION")
        Store.trust_server_certificate = EnvUtil.get_env(
            "TRUST_SERVER_CERTIFICATE"
        )
        Store.connection_string = ""
        Store.cursor = None
