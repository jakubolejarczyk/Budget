from budget.store import BudgetStore
from budget.model import ArgumentModel


class ExitLogic:
    def run(self, name: str, arguments: list[ArgumentModel]) -> None:
        BudgetStore.is_running = False
        BudgetStore.answer = "The application has exited."
