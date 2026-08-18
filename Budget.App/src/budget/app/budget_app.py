from budget.store.budget_store import BudgetStore

class BudgetApp:
    def __init__(self):
        self.budget_store = BudgetStore()

    def run(self):
        while self.budget_store.is_running:
            self.budget_store.command = input("Enter command: ")
            if self.budget_store.command == "exit":
                self.budget_store.is_running = False
            else:
                print(f"The entered command is: {self.budget_store.command}")
