from model import ProgramModel, CommandModel
from program import ExitProgram, HelpProgram


class ProgramConfig:
    def __init__(self: ProgramConfig) -> None:
        self._exit_program = ExitProgram()
        self._help_program = HelpProgram()
        self._config: dict[str, ProgramModel] = {
            "exit": ProgramModel(
                program="exit",
                command={
                    "help": CommandModel(
                        command="help",
                        arguments="arguments",
                        method=self._exit_program.run_help_command
                    )
                },
                arguments="arguments",
                method=self._exit_program.run_program
            ),
            "help": ProgramModel(
                program="help",
                command={},
                arguments="arguments",
                method=self._help_program.run_program
            )
        }

    def get_config(self: ProgramConfig) -> ProgramConfig:
        return self._config
