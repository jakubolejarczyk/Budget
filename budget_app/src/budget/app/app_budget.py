from budget.service import GetInputService, CmdParserService
from budget.store import AppStore


class AppBudget:
    def __init__(self) -> None:
        self._get_imput_service = GetInputService()
        self._cmd_parser_service = CmdParserService()

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
            cmd = self._cmd_parser_service.parse(user_input)
            # TODO: Create the logic to select program based on cmd
            print(cmd)

    def _terminate(self) -> None:
        AppStore.terminate()
