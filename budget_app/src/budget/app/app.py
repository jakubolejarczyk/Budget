from budget.life_cycle import InitLifeCycle, ProcessLifeCycle, TerminateLifeCycle


class App:
    def __init__(self) -> None:
        self._init_life_cycle = InitLifeCycle()
        self._process_life_cycle = ProcessLifeCycle()
        self._terminate_life_cycle = TerminateLifeCycle()

    def run(self) -> None:
        self._init_life_cycle.run()
        self._process_life_cycle.run()
        self._terminate_life_cycle.run()
