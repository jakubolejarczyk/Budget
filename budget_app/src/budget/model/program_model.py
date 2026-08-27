from collections.abc import Callable
from .command_model import CommandModel


class ProgramModel:
    def __init__(self: ProgramModel, program: str, command: dict[CommandModel], arguments: list[str], logic: Callable[[list[str]], str]) -> None:
        self._program = program
        self._command = command
        self._arguments = arguments
        self._logic = logic

    def get_program(self: ProgramModel) -> str:
        return self._program

    def get_command(self: ProgramModel) -> str:
        return self._command

    def get_arguments(self: ProgramModel) -> list[str]:
        return self._arguments

    def get_logic(self: ProgramModel) -> Callable[[list[str]], str]:
        return self._logic
