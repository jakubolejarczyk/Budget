from budget.model import ProgramModel


class BudgetStore:
    is_running: bool
    command: str
    program: ProgramModel

    @staticmethod
    def init() -> None:
        BudgetStore.is_running = True
        BudgetStore._reset()

    @staticmethod
    def terminate() -> None:
        BudgetStore.is_running = False
        BudgetStore._reset()

    @staticmethod
    def _reset() -> None:
        BudgetStore.command = ""
        BudgetStore.program = None
