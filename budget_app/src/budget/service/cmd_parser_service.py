from budget.model import CmdParserModel


class CmdParserService:
    def parse(self, cmd: str) -> CmdParserModel:
        cmd_items: list[str] = cmd.split(" ")
        program: str = self._get_program(cmd_items)
        program_arguments: str = self._get_program_arguments(cmd_items)
        command: str = self._get_command(cmd_items)
        command_arguments = self._get_command_arguments(cmd_items)
        cmd_model: CmdParserModel = CmdParserModel(
            program,
            program_arguments,
            command,
            command_arguments
        )
        return cmd_model

    def _get_program(self, cmd_items: list[str]) -> str:
        if len(cmd_items) == 0:
            return ""
        program = cmd_items[0]
        if self._is_arg(program):
            return ""
        return program

    def _get_program_arguments(self, cmd_items: list[str]) -> list[str]:
        arguments: list[str] = []
        if len(cmd_items) <= 1:
            return []
        for cmd_item in cmd_items[1:]:
            if self._is_arg(cmd_item):
                arguments.append(cmd_item)
            else:
                break
        return arguments

    def _get_command(self, cmd_items: list[str]) -> str:
        if len(cmd_items) <= 1:
            return ""
        for cmd_item in cmd_items[1:]:
            if self._is_arg(cmd_item):
                continue
            return cmd_item
        return ""

    def _get_command_arguments(self, cmd_items: list[str]) -> list[str]:
        arguments: list[str] = []
        if len(cmd_items) <= 1:
            return []
        start_index = 0
        for cmd_item in cmd_items:
            if start_index == 0:
                start_index += 1
                continue
            start_index += 1
            if not self._is_arg(cmd_item):
                break
        for cmd_item in cmd_items[start_index:]:
            if self._is_arg(cmd_item):
                arguments.append(cmd_item)
        return arguments

    def _is_arg(self, cmd_item: str) -> bool:
        if cmd_item.startswith("-") or cmd_item.startswith("--"):
            return True
        return False
