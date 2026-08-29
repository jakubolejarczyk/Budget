from budget.store import BudgetStore


class FetchInputCommandService:
    def fetch(self) -> None:
        BudgetStore.command = self._fetch_input()

    def _fetch_input(self) -> str:
        return input("Enter command: ")
