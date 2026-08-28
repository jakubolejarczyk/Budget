from budget.store import AppStore


class AppBudget:
    def run(self) -> None:
        self._init()
        while AppStore.is_running:
            self._logic()
        self._terminate()

    def _init(self) -> None:
        AppStore.init()

    def _logic(self) -> None:
        while AppStore.is_running:
            command = input("> ")
            if command == "exit":
                AppStore.is_running = False

    def _terminate(self) -> None:
        AppStore.terminate()
