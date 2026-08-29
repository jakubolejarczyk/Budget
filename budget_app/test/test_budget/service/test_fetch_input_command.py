from budget.store import BudgetStore
from budget.service import FetchInputCommandService


class TestFetchInputCommandService:
    def test_should_fetch_input_command_and_set_in_the_store_correctly(self, monkeypatch) -> None:
        fetch_input_command_service = FetchInputCommandService()
        monkeypatch.setattr(
            fetch_input_command_service,
            "_fetch_input",
            self._fake_fetch_input
        )
        BudgetStore.init()
        fetch_input_command_service.fetch()
        received = BudgetStore.command
        expected = "aaa -b --cc --dd=ee fff -g --hh --ii=jj"
        BudgetStore.terminate()
        assert received == expected

    def _fake_fetch_input(self) -> str:
        return "aaa -b --cc --dd=ee fff -g --hh --ii=jj"
