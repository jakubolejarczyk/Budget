# from budget.life_cycle import BudgetLifeCycle
# from budget.store import BudgetStore
# from budget.service import FetchCommandService


# class TestFetchInputCommandService:
#     def test_should_fetch_command_and_set_in_the_store_correctly(self, monkeypatch) -> None:
#         fetch_command_service = FetchCommandService()
#         monkeypatch.setattr(
#             fetch_command_service,
#             "_fetch_input",
#             self._fake_fetch_input
#         )
#         budget_life_cycle = BudgetLifeCycle()
#         budget_life_cycle.init()
#         fetch_command_service.fetch()
#         received = BudgetStore.command
#         expected = "aaa -b --cc --dd=ee fff -g --hh --ii=jj"
#         budget_life_cycle.terminate()
#         assert received == expected

#     def _fake_fetch_input(self) -> str:
#         return "aaa -b --cc --dd=ee fff -g --hh --ii=jj"
