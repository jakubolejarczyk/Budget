from budget.step import InitStoreStep, CreateConnectionStringStep


class InitLifeCycle:
    def __init__(self) -> None:
        self._init_store_step = InitStoreStep()
        self._create_connection_string_step = CreateConnectionStringStep()

    def run(self) -> None:
        self._init_store_step.run()
        self._create_connection_string_step.run()
