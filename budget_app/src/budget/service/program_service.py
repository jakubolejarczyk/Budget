from budget.config import ProgramConfig
from budget.model import ProgramModel
from budget.store import BudgetStore


class ProgramService:
    def run(self) -> None:
        program: ProgramModel = BudgetStore.program
        program_config = ProgramConfig.PROGRAM_CONFIG.get(program.name)
        if program_config is not None:
            program_config.logic(program)
