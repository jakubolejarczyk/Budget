from budget.step import InitStoreStep


class InitLifeCycle:
    def __init__(self) -> None:
        self._init_store_step = InitStoreStep()

    def run(self) -> None:
        self._init_store_step.run()
