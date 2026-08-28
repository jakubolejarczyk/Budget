from budget.service import GetInputService
from budget.store import AppStore


class AppBudget:
    def __init__(self) -> None:
        self._get_imput_service = GetInputService()

    def run(self) -> None:
        self._init()
        while AppStore.is_running:
            self._logic()
        self._terminate()

    def _init(self) -> None:
        AppStore.init()

    def _logic(self) -> None:
        while AppStore.is_running:
            user_input = self._get_imput_service.get_input()
            if user_input == "exit":
                AppStore.is_running = False

    def _terminate(self) -> None:
        AppStore.terminate()
