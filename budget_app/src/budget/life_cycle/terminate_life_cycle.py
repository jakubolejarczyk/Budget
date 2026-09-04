from budget.step import TerminateStoreStep


class TerminateLifeCycle:
    def __init__(self) -> None:
        self._terminate_store_step = TerminateStoreStep()

    def run(self) -> None:
        self._terminate_store_step.run()
