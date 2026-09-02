from budget.store import BudgetStore
from budget.model import ProgramModel


class UnknownProgramLogic:
    def run(self, program: ProgramModel) -> None:
        if not program.name:
            BudgetStore.answer = "The program was not specified."
        else:
            BudgetStore.answer = f"The program '{program.name}' does not exist."
