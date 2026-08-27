from budget.model import CmdParserModel


class CmdParserService:
    def parse(self, cmd: str) -> CmdParserModel:
        cmd_items: list[str] = cmd.split(" ")
        return CmdParserModel(
            program=self._get_program(cmd_items),
            program_args=[],
            command="",
            command_args=[]
        )

    def _get_program(self, cmd_items: list[str]) -> str | None:
        if len(cmd_items) > 0:
            program: str = cmd_items[0]
            if program == "":
                return None
            return program
        return None
