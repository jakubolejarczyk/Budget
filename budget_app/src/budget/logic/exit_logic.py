from budget.store import BudgetStore
from budget.model import ProgramModel


class ExitLogic:
    def run(self, program: ProgramModel) -> None:
        BudgetStore.is_running = False
