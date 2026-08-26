class ExitProgram:
    def run_program(self: ExitProgram, arguments: str) -> str:
        return f"Program: Exit, Command: None, Arguments: {arguments}"

    def run_help_command(self: ExitProgram, arguments: str) -> str:
        return f"Program: Exit, Command: Help, Arguments: {arguments}"
