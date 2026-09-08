from budget.store import Store
from budget.config import ProgramConfig
from budget.model import ProgramConfigModel, CommandConfigModel


class GetProgramStep:
    def run(self) -> None:
        program_config = self._get_program()
        Store.selected_program_config = program_config
        if program_config:
            command_config = self._get_command(program_config)
            if command_config:
                Store.selected_command_config = command_config
            else:
                Store.selected_command_config = None
        else:
            Store.selected_command_config = None

    def _get_program(self) -> ProgramConfigModel:
        for program in ProgramConfig.PROGRAM_CONFIG:
            if program.name == Store.program.name:
                return program
        return None

    def _get_command(self, program_config: ProgramConfigModel) -> CommandConfigModel:
        for command in program_config.commands:
            if command.name == Store.program.command.name:
                return command
        return None
