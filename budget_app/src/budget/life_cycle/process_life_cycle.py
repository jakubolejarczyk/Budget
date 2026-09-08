from budget.store import Store
from budget.step import FetchCommandStep, ParseCommandStep, GetProgramStep


class ProcessLifeCycle:
    def __init__(self) -> None:
        self._fetch_command_step = FetchCommandStep()
        self._parse_command_step = ParseCommandStep()
        self._get_program_step = GetProgramStep()

    def run(self) -> None:
        while Store.is_running:
            self._fetch_command_step.run()
            self._parse_command_step.run()
            self._get_program_step.run()
            print(f"Selected program config: {Store.selected_program_config}")
            print(f"Selected command config: {Store.selected_command_config}")
