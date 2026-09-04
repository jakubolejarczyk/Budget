from .budgets_logic_model import CreateBudgetModel, ReadBudgetModel, UpdateBudgetModel, DeleteBudgetModel


class BudgetsLogic:
    def create_budget(self, model: CreateBudgetModel) -> None:
        pass

    def read_budget(self, model: ReadBudgetModel) -> None:
        pass

    def read_budgets(self) -> None:
        pass

    def update_budget(self, model: UpdateBudgetModel) -> None:
        pass

    def delete_budget(self, model: DeleteBudgetModel) -> None:
        pass
