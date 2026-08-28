from budget.model import CmdParserModel
from budget.service import CmdParserService


class TestCmdParserService:
    def test_should_parse_empty_cmd(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse("")
        expect = CmdParserModel(
            program="",
            program_arguments={},
            command="",
            command_arguments={}
        )
        assert result == expect

    def test_should_parse_cmd_program(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse("aaa")
        expect = CmdParserModel(
            program="aaa",
            program_arguments={},
            command="",
            command_arguments={}
        )
        assert result == expect

    def test_should_parse_cmd_alias(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse("-a")
        expect = CmdParserModel(
            program="",
            program_arguments={},
            command="",
            command_arguments={}
        )
        assert result == expect

    def test_should_parse_cmd_alias_with_value(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse("-a=bbb")
        expect = CmdParserModel(
            program="",
            program_arguments={},
            command="",
            command_arguments={}
        )
        assert result == expect

    def test_should_parse_cmd_argument(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse("--aaa")
        expect = CmdParserModel(
            program="",
            program_arguments={},
            command="",
            command_arguments={}
        )
        assert result == expect

    def test_should_parse_cmd_argument_with_value(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse("--aaa=bbb")
        expect = CmdParserModel(
            program="",
            program_arguments={},
            command="",
            command_arguments={}
        )
        assert result == expect

    def test_should_parse_cmd_program_command(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse("aaa bbb")
        expect = CmdParserModel(
            program="aaa",
            program_arguments={},
            command="bbb",
            command_arguments={}
        )
        assert result == expect

    def test_should_parse_cmd_program_arguments(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse("aaa -a --bbb --ccc=ddd")
        expect = CmdParserModel(
            program="aaa",
            program_arguments={
                "a": {
                    "name": "a",
                    "value": "",
                    "type": "alias"
                },
                "bbb": {
                    "name": "bbb",
                    "value": "",
                    "type": "argument"
                },
                "ccc": {
                    "name": "ccc",
                    "value": "ddd",
                    "type": "argument"
                }
            },
            command="",
            command_arguments={}
        )
        assert result == expect

    def test_should_parse_cmd_program_arguments_command(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse("aaa -a --bbb --ccc=ddd bbb")
        expect = CmdParserModel(
            program="aaa",
            program_arguments={
                "a": {
                    "name": "a",
                    "value": "",
                    "type": "alias"
                },
                "bbb": {
                    "name": "bbb",
                    "value": "",
                    "type": "argument"
                },
                "ccc": {
                    "name": "ccc",
                    "value": "ddd",
                    "type": "argument"
                }
            },
            command="bbb",
            command_arguments={}
        )
        assert result == expect

    def test_should_parse_cmd_program_command_arguments(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse("aaa bbb -a --bbb --ccc=ddd")
        expect = CmdParserModel(
            program="aaa",
            program_arguments={},
            command="bbb",
            command_arguments={
                "a": {
                    "name": "a",
                    "value": "",
                    "type": "alias"
                },
                "bbb": {
                    "name": "bbb",
                    "value": "",
                    "type": "argument"
                },
                "ccc": {
                    "name": "ccc",
                    "value": "ddd",
                    "type": "argument"
                }
            }
        )
        assert result == expect

    def test_should_parse_cmd_program_arguments_command_arguments(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse(
            "aaa -a --bbb --ccc=ddd bbb -a --bbb --ccc=ddd")
        expect = CmdParserModel(
            program="aaa",
            program_arguments={
                "a": {
                    "name": "a",
                    "value": "",
                    "type": "alias"
                },
                "bbb": {
                    "name": "bbb",
                    "value": "",
                    "type": "argument"
                },
                "ccc": {
                    "name": "ccc",
                    "value": "ddd",
                    "type": "argument"
                }
            },
            command="bbb",
            command_arguments={
                "a": {
                    "name": "a",
                    "value": "",
                    "type": "alias"
                },
                "bbb": {
                    "name": "bbb",
                    "value": "",
                    "type": "argument"
                },
                "ccc": {
                    "name": "ccc",
                    "value": "ddd",
                    "type": "argument"
                }
            }
        )
        assert result == expect

    def test_should_parse_cmd_program_arguments_command_arguments_multiple_values(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse(
            "aaa -a=1,2,3,4,5 bbb --bbb=a,b,c,d,e")
        expect = CmdParserModel(
            program="aaa",
            program_arguments={
                "a": {
                    "name": "a",
                    "value": ["1", "2", "3", "4", "5"],
                    "type": "alias"
                }
            },
            command="bbb",
            command_arguments={
                "bbb": {
                    "name": "bbb",
                    "value": ["a", "b", "c", "d", "e"],
                    "type": "argument"
                }
            }
        )
        assert result == expect

    def test_should_parse_cmd_program_arguments_command_arguments_quotation_marks(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse('aaa -a="A" bbb --bbb="BBB"')
        expect = CmdParserModel(
            program="aaa",
            program_arguments={
                "a": {
                    "name": "a",
                    "value": '"A"',
                    "type": "alias"
                }
            },
            command="bbb",
            command_arguments={
                "bbb": {
                    "name": "bbb",
                    "value": '"BBB"',
                    "type": "argument"
                }
            }
        )
        assert result == expect

    def test_should_parse_cmd_program_arguments_command_arguments_command_ignore_last_command(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse(
            'aaa -a --bbb ccc -d --eee fff -g --hhh i -j --kkk')
        expect = CmdParserModel(
            program="aaa",
            program_arguments={
                "a": {
                    "name": "a",
                    "value": "",
                    "type": "alias"
                },
                "bbb": {
                    "name": "bbb",
                    "value": "",
                    "type": "argument"
                }
            },
            command="ccc",
            command_arguments={
                "d": {
                    "name": "d",
                    "value": "",
                    "type": "alias"
                },
                "eee": {
                    "name": "eee",
                    "value": "",
                    "type": "argument"
                },
                "g": {
                    "name": "g",
                    "value": "",
                    "type": "alias"
                },
                "hhh": {
                    "name": "hhh",
                    "value": "",
                    "type": "argument"
                },
                "j": {
                    "name": "j",
                    "value": "",
                    "type": "alias"
                },
                "kkk": {
                    "name": "kkk",
                    "value": "",
                    "type": "argument"
                }
            }
        )
        assert result == expect
