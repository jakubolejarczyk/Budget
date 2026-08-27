from budget.program import HelpProgram


class TestHelpProgram:
    def test_should_run_main_command_correctly(self):
        help_program = HelpProgram()
        result = help_program.run_main_command(["a", "b", "c"])
        expected = "Help main command works with arguments: ['a', 'b', 'c']"
        assert result == expected
