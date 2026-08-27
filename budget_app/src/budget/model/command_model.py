from collections.abc import Callable


class CommandModel:
    def __init__(self: CommandModel, command: str, arguments: list[str], logic: Callable[[list[str]], str]) -> None:
        self._command = command
        self._arguments = arguments
        self._logic = logic

    def get_command(self: CommandModel) -> str:
        return self._command

    def get_arguments(self: CommandModel) -> list[str]:
        return self._arguments

    def get_logic(self: CommandModel) -> Callable[[list[str]], str]:
        return self._logic
