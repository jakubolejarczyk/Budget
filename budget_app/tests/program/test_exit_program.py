from program import ExitProgram


def test_exit_program_run_program() -> None:
    exit_program: ExitProgram = ExitProgram()
    result: str = exit_program.run_program("arguments")
    assert result == "Program: Exit, Command: None, Arguments: arguments"


def test_exit_program_run_help_command() -> None:
    exit_program: ExitProgram = ExitProgram()
    result: str = exit_program.run_help_command("arguments")
    assert result == "Program: Exit, Command: Help, Arguments: arguments"
