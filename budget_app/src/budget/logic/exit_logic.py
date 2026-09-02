from budget.store import BudgetStore


class ExitLogic:
    def run(self) -> None:
        BudgetStore.is_running = False
        BudgetStore.answer = "The application has exited."
