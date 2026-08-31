from budget.model import ProgramModel, CommandModel, ArgumentModel
from budget.store import BudgetStore


class ParseCommandService:
    def parse(self) -> None:
        command_items = BudgetStore.command.split(" ")
        program_name = self._get_program_name(command_items)
        program_arguments = self._get_program_arguments(command_items)
        command_name = self._get_command_name(command_items)
        BudgetStore.program = ProgramModel(
            name=program_name,
            arguments=program_arguments,
            command=CommandModel(
                name=command_name,
                arguments=self._get_command_arguments(command_items)
            )
        )

    def _get_program_name(self, command_items: list[str]) -> str:
        if len(command_items) <= 0:
            return ""
        program_name = command_items[0]
        if self._is_alias(program_name) or self._is_argument(program_name):
            return ""
        return program_name

    def _get_program_arguments(self, command_items: list[str]) -> list[ArgumentModel]:
        arguments: list[ArgumentModel] = []
        if len(command_items) <= 1:
            return arguments
        for command_item in command_items[1:]:
            if self._is_argument(command_item):
                arguments.append(self._create_argument(command_item))
            elif self._is_alias(command_item):
                arguments.append(self._create_alias(command_item))
            else:
                break
        return arguments

    def _get_command_name(self, command_items: list[str]) -> str:
        if len(command_items) <= 1:
            return ""
        for command_item in command_items[1:]:
            if not self._is_alias(command_item) and not self._is_argument(command_item):
                return command_item
        return ""

    def _get_command_arguments(self, command_items: list[str]) -> list[ArgumentModel]:
        arguments: list[ArgumentModel] = []
        if len(command_items) <= 1:
            return arguments
        command_index = 1
        for command_item in command_items[1:]:
            if not self._is_alias(command_item) and not self._is_argument(command_item):
                command_index += 1
                break
            else:
                command_index += 1
        for command_item in command_items[command_index:]:
            if self._is_argument(command_item):
                arguments.append(self._create_argument(command_item))
            elif self._is_alias(command_item):
                arguments.append(self._create_alias(command_item))
        return arguments

    def _is_argument(self, command_item: str) -> bool:
        return command_item.startswith("--")

    def _is_alias(self, command_item: str) -> bool:
        return command_item.startswith("-")

    def _create_argument(self, command_item: str) -> ArgumentModel:
        argument = command_item.replace("--", "")
        name: str
        value: str
        has_value: bool
        has_multiple_values: bool
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
            value = ""
            has_value = False
            has_multiple_values = False
        return ArgumentModel(
            name=name,
            value=value,
            has_value=has_value,
            has_multiple_values=has_multiple_values,
            type="argument"
        )

    def _create_alias(self, command_item: str) -> ArgumentModel:
        alias = command_item.replace("-", "")
        name: str
        value: str
        has_value: bool
        has_multiple_values: bool
        if "=" in alias:
            alias_items = alias.split("=")
            name = alias_items[0]
            value = alias_items[1]
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            has_value = True
            has_multiple_values = False
            if "," in value:
                value = value.split(",")
                has_multiple_values = True
        else:
            name = alias
            value = ""
            has_value = False
            has_multiple_values = False
        return ArgumentModel(
            name=name,
            value=value,
            has_value=has_value,
            has_multiple_values=has_multiple_values,
            type="alias"
        )
