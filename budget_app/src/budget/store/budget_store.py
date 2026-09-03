from mssql_python import Cursor
from os import getenv
from budget.model import ProgramModel


class BudgetStore:
    server: str
    database: str
    encrypt: str
    trusted_connection: str
    trust_server_certificate: str
    is_running: bool
    command: str
    program: ProgramModel
    answer: str
    cursor: Cursor

    @staticmethod
    def init() -> None:
        BudgetStore.server = getenv("SERVER")
        BudgetStore.database = getenv("DATABASE")
        BudgetStore.encrypt = getenv("ENCRYPT")
        BudgetStore.trusted_connection = getenv("TRUSTED_CONNECTION")
        BudgetStore.trust_server_certificate = getenv(
            "TRUST_SERVER_CERTIFICATE"
        )
        BudgetStore.is_running = True
        BudgetStore.command = ""
        BudgetStore.program = None
        BudgetStore.answer = ""
        BudgetStore.cursor = None

    @staticmethod
    def terminate() -> None:
        BudgetStore.server = ""
        BudgetStore.database = ""
        BudgetStore.encrypt = ""
        BudgetStore.trusted_connection = ""
        BudgetStore.trust_server_certificate = ""
        BudgetStore.is_running = False
        BudgetStore.command = ""
        BudgetStore.program = None
        BudgetStore.answer = ""
        BudgetStore.cursor = None
