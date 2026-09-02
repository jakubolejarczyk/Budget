from budget.store import BudgetStore
from budget.logic import ExitLogic


class TestExitLogic:
    def test_exit_logic_should_set_is_running_to_false(self) -> None:
        BudgetStore.init()
        exit_logic = ExitLogic()
        exit_logic.run()
        expected = False
        received = BudgetStore.is_running
        BudgetStore.terminate()
        assert received == expected
