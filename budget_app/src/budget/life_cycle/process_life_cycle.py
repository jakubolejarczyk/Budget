from budget.store import Store
from budget.step import FetchCommandStep, ParseCommandStep


class ProcessLifeCycle:
    def __init__(self) -> None:
        self._fetch_command_step = FetchCommandStep()
        self._parse_command_step = ParseCommandStep()

    def run(self) -> None:
        while Store.is_running:
            self._fetch_command_step.run()
            self._parse_command_step.run()
            print(Store.program)
