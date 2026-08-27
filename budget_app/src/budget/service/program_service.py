from collections.abc import Callable
from budget.config import ProgramConfig
from budget.model import ProgramModel


class ProgramService:
    def __init__(self: ProgramService) -> None:
        self._program_config = ProgramConfig()
        self._program_config.init_config()

    def run_program(self: ProgramService, program: str, command: str, arguments: list[str]) -> str:
        config: dict[str, ProgramModel] = self._program_config.get_config()
        program: ProgramModel = config.get(program)
        logic: Callable[[list[str], str]] = program._logic
        result: str = logic(arguments)
        return result
