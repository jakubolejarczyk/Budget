from budget.life_cycle import BudgetLifeCycle


class BudgetApp:
    def __init__(self) -> None:
        self._budget_life_cycle = BudgetLifeCycle()

    def run(self) -> None:
        self._budget_life_cycle.init()
        self._budget_life_cycle.process()
        self._budget_life_cycle.terminate()
