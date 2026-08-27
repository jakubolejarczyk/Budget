from program import HelpProgram


def test_help_program_run_program() -> None:
    help_program: HelpProgram = HelpProgram()
    result: str = help_program.run_program("arguments")
    assert result == "Program: Help, Command: None, Arguments: arguments"
