from budget.store import AppStore


class ExitLogic:
    def run(self) -> None:
        AppStore.is_running = False
