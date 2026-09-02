from budget.config import ProgramConfig
from budget.store import BudgetStore


class ProgramService:
    def run(self) -> None:
        program = BudgetStore.program
        if program.name in ProgramConfig.PROGRAM_CONFIG:
            logic = ProgramConfig.PROGRAM_CONFIG.get(program.name).logic
            logic(program.name, program.arguments)
        else:
            program_name = "unknown_program"
            logic = ProgramConfig.PROGRAM_CONFIG.get(program_name).logic
            logic(program.name, program.arguments)
