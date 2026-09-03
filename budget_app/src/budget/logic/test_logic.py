from budget.store import BudgetStore
from budget.model import ArgumentModel


class TestLogic:
    def run(self, name: str, arguments: list[ArgumentModel]) -> None:
        BudgetStore.cursor.execute("SELECT * FROM expenses")
        rows = BudgetStore.cursor.fetchall()
        for row in rows:
            print(row)
