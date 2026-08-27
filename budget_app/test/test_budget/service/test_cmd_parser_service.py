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
                "a": "",
                "bbb": "",
                "ccc": "ddd"
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
                "a": "",
                "bbb": "",
                "ccc": "ddd"
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
                "a": "",
                "bbb": "",
                "ccc": "ddd"
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
                "a": "",
                "bbb": "",
                "ccc": "ddd"
            },
            command="bbb",
            command_arguments={
                "a": "",
                "bbb": "",
                "ccc": "ddd"
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
                "a": ["1", "2", "3", "4", "5"]
            },
            command="bbb",
            command_arguments={
                "bbb": ["a", "b", "c", "d", "e"]
            }
        )
        assert result == expect

    def test_should_parse_cmd_program_arguments_command_arguments_quotation_marks(self) -> None:
        cmd_parser_service = CmdParserService()
        result = cmd_parser_service.parse('aaa -a="A" bbb --bbb="BBB"')
        expect = CmdParserModel(
            program="aaa",
            program_arguments={
                'a': '"A"'
            },
            command="bbb",
            command_arguments={
                "bbb": '"BBB"'
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
                "a": "",
                "bbb": ""
            },
            command="ccc",
            command_arguments={
                "d": "",
                "eee": "",
                "g": "",
                "hhh": "",
                "j": "",
                "kkk": ""
            }
        )
        assert result == expect
