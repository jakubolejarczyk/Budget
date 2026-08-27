from budget.program import HelpProgram


class TestHelpProgram:
    def test_should_run_program_correctly(self: TestHelpProgram) -> None:
        help_program: HelpProgram = HelpProgram()
        result: str = help_program.run_program(["a", "b", "c"])
        expected: str = "Help program works with arguments: ['a', 'b', 'c']"
        assert result == expected
