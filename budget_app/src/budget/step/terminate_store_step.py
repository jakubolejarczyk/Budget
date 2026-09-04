from budget.store import Store


class TerminateStoreStep:
    def run(self) -> None:
        Store.terminate()
