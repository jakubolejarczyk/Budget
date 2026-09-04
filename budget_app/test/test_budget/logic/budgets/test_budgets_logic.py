from budget.logic.budgets import BudgetsLogic


class TestBudgetsLogic:
    def test_create_budget(self) -> str:
        budget_logic = BudgetsLogic()
        expected = "create_budget"
        received = budget_logic.create_budget(None)
        assert expected == received

    def test_read_budget(self) -> str:
        budget_logic = BudgetsLogic()
        expected = "read_budget"
        received = budget_logic.read_budget(None)
        assert expected == received

    def test_read_budgets(self) -> str:
        budget_logic = BudgetsLogic()
        expected = "read_budgets"
        received = budget_logic.read_budgets()
        assert expected == received

    def test_update_budget(self) -> str:
        budget_logic = BudgetsLogic()
        expected = "update_budget"
        received = budget_logic.update_budget(None)
        assert expected == received

    def test_delete_budget(self) -> str:
        budget_logic = BudgetsLogic()
        expected = "delete_budget"
        received = budget_logic.delete_budget(None)
        assert expected == received
