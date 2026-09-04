from .budgets_logic_model import CreateBudgetModel, ReadBudgetModel, UpdateBudgetModel, DeleteBudgetModel


class BudgetsLogic:
    def create_budget(self, model: CreateBudgetModel) -> str:
        return "create_budget"

    def read_budget(self, model: ReadBudgetModel) -> str:
        return "read_budget"

    def read_budgets(self) -> str:
        return "read_budgets"

    def update_budget(self, model: UpdateBudgetModel) -> str:
        return "update_budget"

    def delete_budget(self, model: DeleteBudgetModel) -> str:
        return "delete_budget"
