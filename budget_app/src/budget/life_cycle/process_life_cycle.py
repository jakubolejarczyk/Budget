from budget.store import Store
from budget.step import FetchCommandStep, ParseCommandStep, GetProgramStep, CheckArgumentsStep, InitStoreStep
from budget.util import ColorUtil, ConsoleColor


class ProcessLifeCycle:
    def __init__(self) -> None:
        self._init_store_step = InitStoreStep()
        self._fetch_command_step = FetchCommandStep()
        self._parse_command_step = ParseCommandStep()
        self._get_program_step = GetProgramStep()
        self._check_arguments_step = CheckArgumentsStep()

    def run(self) -> None:
        while Store.is_running:
            self._init_store_step.run()
            self._fetch_command_step.run()
            self._parse_command_step.run()
            self._get_program_step.run()
            self._check_arguments_step.run(
                Store.selected_program_config,
                Store.program.arguments
            )
            self._check_arguments_step.run(
                Store.selected_command_config,
                Store.program.command.arguments
            )
            ColorUtil.set_color(ConsoleColor.GRAY)
            print(f"Are arguments correct: {Store.are_arguments_correct}")
            ColorUtil.set_color(ConsoleColor.RESET)
