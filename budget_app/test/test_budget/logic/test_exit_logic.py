from budget.logic import ExitLogic
from budget.store import AppStore


class TestExitLogic:
    def test_should_exit_the_program_correctly(self):
        AppStore.init()
        exit_logic = ExitLogic()
        exit_logic.run()
        expected = False
        received = AppStore.is_running
        assert expected == received
