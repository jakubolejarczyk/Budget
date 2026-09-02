from budget.store import BudgetStore
from budget.service import FetchCommandService, ParseCommandService, ProgramService


class BudgetLifeCycle:
    def __init__(self):
        self._fetch_command_service = FetchCommandService()
        self._parse_command_service = ParseCommandService()
        self._program_service = ProgramService()

    def init(self) -> None:
        BudgetStore.init()

    def process(self) -> None:
        while BudgetStore.is_running:
            self._fetch_command_service.fetch()
            self._parse_command_service.parse()
            self._program_service.run()
            print(BudgetStore.answer)

    def terminate(self) -> None:
        BudgetStore.terminate()
