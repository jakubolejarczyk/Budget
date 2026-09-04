from budget.store import Store


class FetchCommandStep:
    def run(self) -> None:
        Store.command = self._fetch_input()

    def _fetch_input(self) -> str:
        return input("Enter command: ")
