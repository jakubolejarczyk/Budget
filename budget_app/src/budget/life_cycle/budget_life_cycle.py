from budget.store import BudgetStore


class BudgetLifeCycle:
    def init(self) -> None:
        BudgetStore.init()

    def process(self) -> None:
        print(BudgetStore.is_running)

    def terminate(self) -> None:
        BudgetStore.terminate()
