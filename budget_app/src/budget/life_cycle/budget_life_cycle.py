from budget.store import BudgetStore
from budget.service import FetchInputCommandService


class BudgetLifeCycle:
    def __init__(self):
        self._fetch_input_command_service = FetchInputCommandService()

    def init(self) -> None:
        BudgetStore.init()

    def process(self) -> None:
        while BudgetStore.is_running:
            self._fetch_input_command_service.fetch()
            print(f"Result: {BudgetStore.command}")

    def terminate(self) -> None:
        BudgetStore.terminate()
