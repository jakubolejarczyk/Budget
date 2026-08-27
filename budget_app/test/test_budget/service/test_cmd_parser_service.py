from budget.model import CmdParserModel
from budget.service import CmdParserService


class TestCmdParserService:
    def test_should_parse_empty_cmd(self):
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse("")
        expect = CmdParserModel(
            program="",
            program_args=[],
            command="",
            command_args=[]
        )
        assert result == expect
