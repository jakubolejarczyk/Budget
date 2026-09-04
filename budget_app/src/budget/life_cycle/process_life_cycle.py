from budget.store import Store
from budget.step import FetchCommandStep


class ProcessLifeCycle:
    def __init__(self) -> None:
        self._fetch_command_step = FetchCommandStep()

    def run(self) -> None:
        while Store.is_running:
            self._fetch_command_step.run()
            print(Store.command)
