from budget.service import ParseCommandService
from budget.store import BudgetStore
from budget.model import ProgramModel, CommandModel, ArgumentModel


class TestParseCommandService:
    def test_should_parse_empty_command_to_empty_model(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = ""
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="",
            arguments=[],
            command=CommandModel(
                name="",
                arguments=[]
            )
        )
        BudgetStore.terminate()
        assert received == expected

    def test_should_parse_command_to_model_with_program(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = "aaa"
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="aaa",
            arguments=[],
            command=CommandModel(
                name="",
                arguments=[]
            )
        )
        BudgetStore.terminate()
        assert received == expected

    def test_should_skip_program_name_when_is_alias(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = "-a"
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="",
            arguments=[],
            command=CommandModel(
                name="",
                arguments=[]
            )
        )
        BudgetStore.terminate()
        assert received == expected

    def test_should_skip_program_name_when_is_alias_with_value(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = "-a=b"
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="",
            arguments=[],
            command=CommandModel(
                name="",
                arguments=[]
            )
        )
        BudgetStore.terminate()
        assert received == expected

    def test_should_skip_program_name_when_is_alias_with_multiple_values(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = "-a=b,c,d"
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="",
            arguments=[],
            command=CommandModel(
                name="",
                arguments=[]
            )
        )
        BudgetStore.terminate()
        assert received == expected

    def test_should_skip_program_name_when_is_argument(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = "--aaa"
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="",
            arguments=[],
            command=CommandModel(
                name="",
                arguments=[]
            )
        )
        BudgetStore.terminate()
        assert received == expected

    def test_should_skip_program_name_when_is_argument_with_value(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = "--aaa=bbb"
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="",
            arguments=[],
            command=CommandModel(
                name="",
                arguments=[]
            )
        )
        BudgetStore.terminate()
        assert received == expected

    def test_should_skip_program_name_when_is_argument_with_multiple_values(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = "--aaa=bbb,ccc,ddd"
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="",
            arguments=[],
            command=CommandModel(
                name="",
                arguments=[]
            )
        )
        BudgetStore.terminate()
        assert received == expected

    def test_should_parse_command_to_model_with_program_command(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = "aaa bbb"
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="aaa",
            arguments=[],
            command=CommandModel(
                name="bbb",
                arguments=[]
            )
        )
        BudgetStore.terminate()
        assert received == expected

    def test_should_parse_command_to_model_with_program_arguments(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = "aaa -a -b=c -d=e,f,g --hhh --iii=jjj --kkk=lll,mmm,nnn"
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="aaa",
            arguments=[
                ArgumentModel(
                    name="a",
                    value="",
                    has_value=False,
                    has_multiple_values=False,
                    type="alias"
                ),
                ArgumentModel(
                    name="b",
                    value="c",
                    has_value=True,
                    has_multiple_values=False,
                    type="alias"
                ),
                ArgumentModel(
                    name="d",
                    value=["e", "f", "g"],
                    has_value=True,
                    has_multiple_values=True,
                    type="alias"
                ),
                ArgumentModel(
                    name="hhh",
                    value="",
                    has_value=False,
                    has_multiple_values=False,
                    type="argument"
                ),
                ArgumentModel(
                    name="iii",
                    value="jjj",
                    has_value=True,
                    has_multiple_values=False,
                    type="argument"
                ),
                ArgumentModel(
                    name="kkk",
                    value=["lll", "mmm", "nnn"],
                    has_value=True,
                    has_multiple_values=True,
                    type="argument"
                ),
            ],
            command=CommandModel(
                name="",
                arguments=[]
            )
        )
        BudgetStore.terminate()
        assert received == expected

    def test_should_parse_command_to_model_with_program_arguments_command(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = "aaa -a -b=c -d=e,f,g --hhh --iii=jjj --kkk=lll,mmm,nnn bbb"
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="aaa",
            arguments=[
                ArgumentModel(
                    name="a",
                    value="",
                    has_value=False,
                    has_multiple_values=False,
                    type="alias"
                ),
                ArgumentModel(
                    name="b",
                    value="c",
                    has_value=True,
                    has_multiple_values=False,
                    type="alias"
                ),
                ArgumentModel(
                    name="d",
                    value=["e", "f", "g"],
                    has_value=True,
                    has_multiple_values=True,
                    type="alias"
                ),
                ArgumentModel(
                    name="hhh",
                    value="",
                    has_value=False,
                    has_multiple_values=False,
                    type="argument"
                ),
                ArgumentModel(
                    name="iii",
                    value="jjj",
                    has_value=True,
                    has_multiple_values=False,
                    type="argument"
                ),
                ArgumentModel(
                    name="kkk",
                    value=["lll", "mmm", "nnn"],
                    has_value=True,
                    has_multiple_values=True,
                    type="argument"
                ),
            ],
            command=CommandModel(
                name="bbb",
                arguments=[]
            )
        )
        BudgetStore.terminate()
        assert received == expected

    def test_should_parse_command_to_model_with_program_command_arguments(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = "aaa bbb -a -b=c -d=e,f,g --hhh --iii=jjj --kkk=lll,mmm,nnn"
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="aaa",
            arguments=[],
            command=CommandModel(
                name="bbb",
                arguments=[
                    ArgumentModel(
                        name="a",
                        value="",
                        has_value=False,
                        has_multiple_values=False,
                        type="alias"
                    ),
                    ArgumentModel(
                        name="b",
                        value="c",
                        has_value=True,
                        has_multiple_values=False,
                        type="alias"
                    ),
                    ArgumentModel(
                        name="d",
                        value=["e", "f", "g"],
                        has_value=True,
                        has_multiple_values=True,
                        type="alias"
                    ),
                    ArgumentModel(
                        name="hhh",
                        value="",
                        has_value=False,
                        has_multiple_values=False,
                        type="argument"
                    ),
                    ArgumentModel(
                        name="iii",
                        value="jjj",
                        has_value=True,
                        has_multiple_values=False,
                        type="argument"
                    ),
                    ArgumentModel(
                        name="kkk",
                        value=["lll", "mmm", "nnn"],
                        has_value=True,
                        has_multiple_values=True,
                        type="argument"
                    ),
                ]
            )
        )
        BudgetStore.terminate()
        assert received == expected

    def test_should_parse_command_to_model_with_program_arguments_command_arguments(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = "aaa -a -b=c -d=e,f,g --hhh --iii=jjj --kkk=lll,mmm,nnn bbb -a -b=c -d=e,f,g --hhh --iii=jjj --kkk=lll,mmm,nnn"
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="aaa",
            arguments=[
                ArgumentModel(
                    name="a",
                    value="",
                    has_value=False,
                    has_multiple_values=False,
                    type="alias"
                ),
                ArgumentModel(
                    name="b",
                    value="c",
                    has_value=True,
                    has_multiple_values=False,
                    type="alias"
                ),
                ArgumentModel(
                    name="d",
                    value=["e", "f", "g"],
                    has_value=True,
                    has_multiple_values=True,
                    type="alias"
                ),
                ArgumentModel(
                    name="hhh",
                    value="",
                    has_value=False,
                    has_multiple_values=False,
                    type="argument"
                ),
                ArgumentModel(
                    name="iii",
                    value="jjj",
                    has_value=True,
                    has_multiple_values=False,
                    type="argument"
                ),
                ArgumentModel(
                    name="kkk",
                    value=["lll", "mmm", "nnn"],
                    has_value=True,
                    has_multiple_values=True,
                    type="argument"
                ),
            ],
            command=CommandModel(
                name="bbb",
                arguments=[
                    ArgumentModel(
                        name="a",
                        value="",
                        has_value=False,
                        has_multiple_values=False,
                        type="alias"
                    ),
                    ArgumentModel(
                        name="b",
                        value="c",
                        has_value=True,
                        has_multiple_values=False,
                        type="alias"
                    ),
                    ArgumentModel(
                        name="d",
                        value=["e", "f", "g"],
                        has_value=True,
                        has_multiple_values=True,
                        type="alias"
                    ),
                    ArgumentModel(
                        name="hhh",
                        value="",
                        has_value=False,
                        has_multiple_values=False,
                        type="argument"
                    ),
                    ArgumentModel(
                        name="iii",
                        value="jjj",
                        has_value=True,
                        has_multiple_values=False,
                        type="argument"
                    ),
                    ArgumentModel(
                        name="kkk",
                        value=["lll", "mmm", "nnn"],
                        has_value=True,
                        has_multiple_values=True,
                        type="argument"
                    ),
                ]
            )
        )
        BudgetStore.terminate()
        assert received == expected

    def test_should_parse_command_to_model_with_program_arguments_quotation_marks(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = "aaa -b='c' --iii=\"jjj\""
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="aaa",
            arguments=[
                ArgumentModel(
                    name="b",
                    value="c",
                    has_value=True,
                    has_multiple_values=False,
                    type="alias"
                ),
                ArgumentModel(
                    name="iii",
                    value="jjj",
                    has_value=True,
                    has_multiple_values=False,
                    type="argument"
                ),
            ],
            command=CommandModel(
                name="",
                arguments=[]
            )
        )
        BudgetStore.terminate()
        assert received == expected

    def test_should_parse_command_to_model_with_program_command_arguments_ignore_too_many_commands(self) -> None:
        parse_command_service = ParseCommandService()
        BudgetStore.init()
        BudgetStore.command = "aaa bbb -a -b=c -d=e,f,g ccc --hhh --iii=jjj ddd --kkk=lll,mmm,nnn eee"
        parse_command_service.parse()
        received = BudgetStore.program
        expected = ProgramModel(
            name="aaa",
            arguments=[],
            command=CommandModel(
                name="bbb",
                arguments=[
                    ArgumentModel(
                        name="a",
                        value="",
                        has_value=False,
                        has_multiple_values=False,
                        type="alias"
                    ),
                    ArgumentModel(
                        name="b",
                        value="c",
                        has_value=True,
                        has_multiple_values=False,
                        type="alias"
                    ),
                    ArgumentModel(
                        name="d",
                        value=["e", "f", "g"],
                        has_value=True,
                        has_multiple_values=True,
                        type="alias"
                    ),
                    ArgumentModel(
                        name="hhh",
                        value="",
                        has_value=False,
                        has_multiple_values=False,
                        type="argument"
                    ),
                    ArgumentModel(
                        name="iii",
                        value="jjj",
                        has_value=True,
                        has_multiple_values=False,
                        type="argument"
                    ),
                    ArgumentModel(
                        name="kkk",
                        value=["lll", "mmm", "nnn"],
                        has_value=True,
                        has_multiple_values=True,
                        type="argument"
                    ),
                ]
            )
        )
        BudgetStore.terminate()
        assert received == expected
