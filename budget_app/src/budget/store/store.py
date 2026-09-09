from mssql_python import Cursor
from budget.model import ProgramModel, ProgramConfigModel, CommandConfigModel


class Store:
    server: str
    database: str
    encrypt: str
    trusted_connection: str
    trust_server_certificate: str
    connection_string: str
    cursor: Cursor
    is_running: bool
    command: str
    program: ProgramModel
    selected_program_config: ProgramConfigModel
    selected_command_config: CommandConfigModel
    are_arguments_correct: bool
