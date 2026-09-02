from budget.store import BudgetStore
from budget.model import ArgumentModel


class UnknownProgramLogic:
    def run(self, name: str, arguments: list[ArgumentModel]) -> None:
        if not name:
            BudgetStore.answer = "The program was not specified."
        else:
            BudgetStore.answer = f"The program '{name}' does not exist."
