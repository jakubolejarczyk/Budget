class ExitProgram:
    def run_program(self: ExitProgram, arguments: list[str]) -> str:
        return f"Exit program works with arguments: {arguments}"

    def run_help_command(self: ExitProgram, arguments: list[str]) -> str:
        return f"Exit help command works with arguments: {arguments}"
