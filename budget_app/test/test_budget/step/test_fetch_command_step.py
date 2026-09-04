from budget.life_cycle import InitLifeCycle, TerminateStoreStep
from budget.store import Store
from budget.step import FetchCommandStep


class TestFetchCommandStep:
    def test_should_fetch_command_and_set_in_the_store_correctly(self, monkeypatch) -> None:
        InitLifeCycle().run()
        fetch_command_step = FetchCommandStep()
        monkeypatch.setattr(
            fetch_command_step,
            "_fetch_input",
            self._fake_fetch_input
        )
        fetch_command_step.run()
        received = Store.command
        expected = "aaa -b --cc --dd=ee fff -g --hh --ii=jj"
        TerminateStoreStep().run()
        assert received == expected

    def _fake_fetch_input(self) -> str:
        return "aaa -b --cc --dd=ee fff -g --hh --ii=jj"
