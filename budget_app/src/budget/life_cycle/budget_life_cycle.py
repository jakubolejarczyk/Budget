from budget.store import BudgetStore
from budget.service import FetchCommandService


class BudgetLifeCycle:
    def __init__(self):
        self._fetch_command_service = FetchCommandService()

    def init(self) -> None:
        BudgetStore.init()

    def process(self) -> None:
        while BudgetStore.is_running:
            self._fetch_command_service.fetch()
            print(f"Result: {BudgetStore.command}")

    def terminate(self) -> None:
        BudgetStore.terminate()
