from budget.store import BudgetStore
from budget.logic import UnknownProgramLogic


class TestUnknownProgramLogic:
    def test_unknown_program_logic_should_set_answer_correctly(self) -> None:
        BudgetStore.init()
        unknown_program_logic = UnknownProgramLogic()
        unknown_program_logic.run("aaa", [])
        expected = f"The program 'aaa' does not exist."
        received = BudgetStore.answer
        BudgetStore.terminate()
        assert received == expected

    def test_unknown_program_logic_should_set_answer_correctly_when_program_is_empty_string(self) -> None:
        BudgetStore.init()
        unknown_program_logic = UnknownProgramLogic()
        unknown_program_logic.run("", [])
        expected = f"The program was not specified."
        received = BudgetStore.answer
        BudgetStore.terminate()
        assert received == expected
