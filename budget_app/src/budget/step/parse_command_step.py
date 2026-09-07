from budget.model import ProgramModel, CommandModel, ArgumentModel
from budget.store import Store


class ParseCommandStep:
    def run(self) -> None:
        command_items = Store.command.split()
        Store.program = ProgramModel(
            name=self._get_program_name(command_items),
            arguments=self._get_program_arguments(command_items),
            command=CommandModel(
                name=self._get_command_name(command_items),
                arguments=self._get_command_arguments(command_items)
            )
        )

    def _get_program_name(self, command_items: list[str]) -> str | None:
        if len(command_items) <= 0:
            return None
        program_name = command_items[0]
        if self._is_argument(program_name) or self._is_alias(program_name):
            return None
        return program_name

    def _get_program_arguments(self, command_items: list[str]) -> list[ArgumentModel]:
        arguments: list[ArgumentModel] = []
        if len(command_items) <= 1:
            return arguments
        for command_item in command_items[1:]:
            if self._is_argument(command_item):
                argument = self._create_argument_alias(command_item, "--")
                arguments.append(argument)
            elif self._is_alias(command_item):
                alias = self._create_argument_alias(command_item, "-")
                arguments.append(alias)
            else:
                break
        return arguments

    def _get_command_name(self, command_items: list[str]) -> str | None:
        if len(command_items) <= 1:
            return None
        for command_item in command_items[1:]:
            if not self._is_argument(command_item) and not self._is_alias(command_item):
                return command_item
        return None

    def _get_command_arguments(self, command_items: list[str]) -> list[ArgumentModel]:
        arguments: list[ArgumentModel] = []
        if len(command_items) <= 2:
            return arguments
        command_index = 1
        for command_item in command_items[1:]:
            command_index += 1
            if not self._is_alias(command_item) and not self._is_argument(command_item):
                break
        for command_item in command_items[command_index:]:
            if self._is_argument(command_item):
                argument = self._create_argument_alias(command_item, "--")
                arguments.append(argument)
            elif self._is_alias(command_item):
                alias = self._create_argument_alias(command_item, "-")
                arguments.append(alias)
        return arguments

    def _is_argument(self, command_item: str) -> bool:
        return command_item.startswith("--")

    def _is_alias(self, command_item: str) -> bool:
        return command_item.startswith("-")

    def _create_argument_alias(self, command_item: str, prefix: str) -> ArgumentModel:
        argument = command_item.replace(prefix, "")
        name: str
        value: str | list[str] | None
        has_value: bool
        has_multiple_values: bool
        type: str
        if "=" in argument:
            argument_items = argument.split("=")
            name = argument_items[0]
            value = argument_items[1]
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            has_value = True
            has_multiple_values = False
            if "," in value:
                value = value.split(",")
                has_multiple_values = True
        else:
            name = argument
            value = None
            has_value = False
            has_multiple_values = False
        if prefix == "--":
            type = "argument"
        else:
            type = "alias"
        return ArgumentModel(
            name=name,
            value=value,
            has_value=has_value,
            has_multiple_values=has_multiple_values,
            type=type
        )
