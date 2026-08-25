from program import ExitProgram


def test_exit_program_run():
    exit_program = ExitProgram()
    result = exit_program.run("command", "arguments")
    assert result == "command arguments"
