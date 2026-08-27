from budget.program import ExitProgram


class TestExitProgram:
    def test_should_run_main_command_correctly(self):
        exit_program = ExitProgram()
        result = exit_program.run_main_command(["a", "b", "c"])
        expected = "Exit main command works with arguments: ['a', 'b', 'c']"
        assert result == expected

    def test_should_run_help_command_correctly(self):
        exit_program = ExitProgram()
        result = exit_program.run_help_command(["a", "b", "c"])
        expected = "Exit help command works with arguments: ['a', 'b', 'c']"
        assert result == expected
