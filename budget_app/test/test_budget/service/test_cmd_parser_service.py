from budget.model import CmdParserModel
from budget.service import CmdParserService


class TestCmdParserService:
    def test_should_parse_empty_cmd(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse("")
        expect = CmdParserModel(
            program=None,
            program_args=[],
            command="",
            command_args=[]
        )
        assert result == expect

    def test_should_parse_when_only_program_is_provided(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse("aaa")
        expect = CmdParserModel(
            program="aaa",
            program_args=[],
            command="",
            command_args=[]
        )
        assert result == expect
