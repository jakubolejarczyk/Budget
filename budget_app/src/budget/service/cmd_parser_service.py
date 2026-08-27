from budget.model import CmdParserModel


class CmdParserService:
    def parse(self, cmd: str) -> CmdParserModel:
        cmd_items: list[str] = cmd.split(" ")
        return CmdParserModel(
            program=self._get_program(cmd_items),
            program_args=self._get_program_arguments(cmd_items),
            command=self._get_command(cmd_items),
            command_args=self._get_command_arguments(cmd_items)
        )

    def _get_program(self, cmd_items: list[str]) -> str | None:
        if len(cmd_items) > 0:
            program: str = cmd_items[0]
            if program == "" or self._is_arg(program):
                return None
            return program
        return None

    def _get_program_arguments(self, cmd_items: list[str]) -> list[str] | None:
        args: list[str] = []
        if len(cmd_items) < 1:
            return None
        for cmd_item in cmd_items[1:]:
            if self._is_arg(cmd_item):
                args.append(cmd_item)
            else:
                break
        return args

    def _get_command(self, cmd_items: list[str]) -> str | None:
        if len(cmd_items) < 1:
            return None
        for cmd_item in cmd_items[1:]:
            if self._is_arg(cmd_item):
                continue
            return cmd_item
        return None

    def _get_command_arguments(self, cmd_items: list[str]) -> list[str] | None:
        args: list[str] = []
        if len(cmd_items) < 1:
            return None
        index = 1
        for cmd_item in cmd_items[1:]:
            index += 1
            if not self._is_arg(cmd_item):
                break
        for cmd_item in cmd_items[index:]:
            if self._is_arg(cmd_item):
                args.append(cmd_item)
            else:
                break
        return args

    def _is_arg(self, cmd_item: str) -> bool:
        if cmd_item.startswith("-") or cmd_item.startswith("--"):
            return True
        return False
