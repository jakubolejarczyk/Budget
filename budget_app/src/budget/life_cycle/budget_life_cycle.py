from dotenv import load_dotenv
from budget.database import ConnectionDatabase
from budget.store import BudgetStore
from budget.service import FetchCommandService, ParseCommandService, ProgramService


class BudgetLifeCycle:
    def __init__(self):
        self._connection_database = ConnectionDatabase()
        self._fetch_command_service = FetchCommandService()
        self._parse_command_service = ParseCommandService()
        self._program_service = ProgramService()

    def init(self) -> None:
        load_dotenv()
        BudgetStore.init()
        self._connection_database.create_connection()

    def process(self) -> None:
        while BudgetStore.is_running:
            self._fetch_command_service.fetch()
            self._parse_command_service.parse()
            self._program_service.run()
            if BudgetStore.answer is not None:
                print(BudgetStore.answer)
                BudgetStore.answer = ""

    def terminate(self) -> None:
        BudgetStore.terminate()
