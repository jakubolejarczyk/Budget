from service import ProgramService


def test_program_service_run_command():
    program_service: ProgramService = ProgramService()
    result = program_service.run_command("exit", "", "arguments")
    assert result == "Program: Exit, Command: None, Arguments: arguments"
