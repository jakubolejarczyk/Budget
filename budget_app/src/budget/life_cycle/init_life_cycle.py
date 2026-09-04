from budget.step import LoadEnvStep, InitStoreStep, CreateConnectionStringStep, ConnectToDatabaseStep


class InitLifeCycle:
    def __init__(self) -> None:
        self._load_env_step = LoadEnvStep()
        self._init_store_step = InitStoreStep()
        self._create_connection_string_step = CreateConnectionStringStep()
        self._connect_to_database_step = ConnectToDatabaseStep()

    def run(self) -> None:
        self._load_env_step.run()
        self._init_store_step.run()
        self._create_connection_string_step.run()
        self._connect_to_database_step.run()
