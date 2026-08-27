from budget.model import CmdParserModel


class CmdParserService:
    def parse(self, cmd: str) -> CmdParserModel:
        cmd_items: list[str] = cmd.split(" ")
        return CmdParserModel(
            program=self._get_program(cmd_items),
            program_args=[],
            command=self._get_command(cmd_items),
            command_args=[]
        )

    def _get_program(self, cmd_items: list[str]) -> str | None:
        if len(cmd_items) > 0:
            program: str = cmd_items[0]
            if program == "" or self._is_arg(program):
                return None
            return program
        return None

    def _get_command(self, cmd_items: list[str]) -> str | None:
        if len(cmd_items) < 1:
            return None
        for cmd_item in cmd_items[1:]:
            if self._is_arg(cmd_item):
                continue
            return cmd_item
        return None

    def _is_arg(self, cmd_item: str) -> bool:
        if cmd_item.startswith("-") or cmd_item.startswith("--"):
            return True
        return False
