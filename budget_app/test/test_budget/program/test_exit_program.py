from budget.program import ExitProgram


class TestExitProgram:
    def test_should_run_program_correctly(self: TestExitProgram) -> None:
        exit_program: ExitProgram = ExitProgram()
        result: str = exit_program.run_program(["a", "b", "c"])
        expected: str = "Exit program works with arguments: ['a', 'b', 'c']"
        assert result == expected

    def test_should_run_help_command_correctly(self: TestExitProgram) -> None:
        exit_program: ExitProgram = ExitProgram()
        result: str = exit_program.run_help_command(["a", "b", "c"])
        expected: str = "Exit help command works with arguments: ['a', 'b', 'c']"
        assert result == expected
