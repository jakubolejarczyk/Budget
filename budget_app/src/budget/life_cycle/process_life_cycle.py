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
            if Store.are_arguments_correct == False:
                continue
            ColorUtil.set_color(ConsoleColor.GRAY)
            args = self._aaa()
            Store.selected_program_config.logic(args)
            ColorUtil.set_color(ConsoleColor.RESET)

    def _aaa(self):
        args = {
            "program_arguments": {},
            "command_argument": {}
        }
        for program_argument in Store.program.arguments:
            args["program_arguments"][program_argument.name] = program_argument.value
        for command_argument in Store.program.command.arguments:
            args["command_argument"][command_argument.name] = command_argument.value
        return args
