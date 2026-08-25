from program import HelpProgram


def test_help_program_run():
    help_program = HelpProgram()
    result = help_program.run("command", "arguments")
    assert result == "command arguments"
