from budget.store import Store
from budget.step import FetchCommandStep, ParseCommandStep, GetProgramStep, CheckArgumentsStep


class ProcessLifeCycle:
    def __init__(self) -> None:
        self._fetch_command_step = FetchCommandStep()
        self._parse_command_step = ParseCommandStep()
        self._get_program_step = GetProgramStep()
        self._check_arguments_step = CheckArgumentsStep()

    def run(self) -> None:
        while Store.is_running:
            self._fetch_command_step.run()
            self._parse_command_step.run()
            self._get_program_step.run()
            self._check_arguments_step.run(
                Store.program.arguments,
                Store.selected_program_config
            )
            self._check_arguments_step.run(
                Store.program.command.arguments,
                Store.selected_command_config
            )
            print(f"Are arguments correct: {Store.are_arguments_correct}")
