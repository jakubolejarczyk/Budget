from budget.store import AppStore


class ExitLogic:
    def run(self):
        AppStore.is_running = False
