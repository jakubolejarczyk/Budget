from budget.life_cycle import BudgetLifeCycle
from budget.store import BudgetStore
from budget.logic import ExitLogic


class TestExitLogic:
    def test_exit_logic_should_set_is_running_to_false(self) -> None:
        budget_life_cycle = BudgetLifeCycle()
        budget_life_cycle.init()
        exit_logic = ExitLogic()
        exit_logic.run("exit", [])
        expected = False
        received = BudgetStore.is_running
        budget_life_cycle.terminate()
        assert received == expected

    def test_exit_logic_should_set_answer_correctly(self) -> None:
        budget_life_cycle = BudgetLifeCycle()
        budget_life_cycle.init()
        exit_logic = ExitLogic()
        exit_logic.run("exit", [])
        expected = "The application has exited."
        received = BudgetStore.answer
        budget_life_cycle.terminate()
        assert received == expected
