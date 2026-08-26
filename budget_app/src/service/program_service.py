from config import ProgramConfig
from model import ProgramModel, CommandModel


class ProgramService:
    def __init__(self: ProgramService) -> None:
        self._program_config = ProgramConfig()

    def run_command(self: ProgramService, program: str, command: str, arguments: str) -> str:
        config: ProgramConfig = self._program_config.get_config()
        config_program: ProgramModel = config[program]
        program_command = config_program.command.get(command)
        if not program_command:
            return config_program.method(arguments)
        else:
            return program_command.method(arguments)
