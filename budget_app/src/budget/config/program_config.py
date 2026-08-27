from budget.program import ExitProgram, HelpProgram
from budget.model import ProgramModel, CommandModel


class ProgramConfig:
    def __init__(self: ProgramConfig) -> None:
        self._exit_program = ExitProgram()
        self._help_program = HelpProgram()

    def init_config(self: ProgramConfig) -> None:
        self._config: dict[str, ProgramModel] = {
            "exit": ProgramModel(
                program="exit",
                command={
                    "help": CommandModel(
                        command="help",
                        arguments=["a", "b", "c"],
                        logic=self._exit_program.run_help_command
                    )
                },
                arguments=["a", "b", "c"],
                logic=self._exit_program.run_program
            ),
            "help": ProgramModel(
                program="help",
                command={},
                arguments=["a", "b", "c"],
                logic=self._help_program.run_program
            )
        }

    def get_config(self: ProgramModel) -> ProgramConfig:
        return self._config
