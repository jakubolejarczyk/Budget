from budget.model import ProgramModel, CommandModel
from budget.store import BudgetStore
from budget.service import ProgramService


class TestProgramService:
    def test_should_run_exit_program(self) -> None:
        BudgetStore.init()
        BudgetStore.program = ProgramModel(
            name="exit",
            arguments=[],
            command=CommandModel(
                name="",
                arguments=[]
            )
        )
        program_service = ProgramService()
        program_service.run()
        expected = "The application has exited."
        received = BudgetStore.answer
        BudgetStore.terminate()
        assert received == expected

    def test_should_run_unknown_program(self) -> None:
        BudgetStore.init()
        BudgetStore.program = ProgramModel(
            name="",
            arguments=[],
            command=CommandModel(
                name="",
                arguments=[]
            )
        )
        program_service = ProgramService()
        program_service.run()
        expected = "The program was not specified."
        received = BudgetStore.answer
        BudgetStore.terminate()
        assert received == expected
