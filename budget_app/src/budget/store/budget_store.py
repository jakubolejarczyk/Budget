class BudgetStore:
    is_running: bool

    @staticmethod
    def init() -> None:
        BudgetStore.is_running = True

    @staticmethod
    def terminate() -> None:
        BudgetStore.is_running = False
