from budget.model import CmdParserModel


class CmdParserService:
    def parse(self, cmd: str) -> CmdParserModel:
        return CmdParserModel(
            program="",
            program_args=[],
            command="",
            command_args=[]
        )
