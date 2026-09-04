from budget.store import Store


class FetchCommandStep:
    def run(self) -> None:
        Store.command = input("Enter command: ")
