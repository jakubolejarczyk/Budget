from budget.model import ArgumentModel, ProgramConfigModel, CommandConfigModel, ArgumentConfigModel
from budget.store import Store


class CheckArgumentsStep:
    def run(self, config: ProgramConfigModel | CommandConfigModel, arguments: list[ArgumentModel]) -> None:
        Store.are_arguments_correct = True
        config_arguments: list[ArgumentConfigModel] = []
        if config:
            config_arguments = config.arguments
        for config_argument in config_arguments:
            self._check_argument(config_argument, arguments)

    def _check_argument(self, config_argument: ArgumentConfigModel, arguments: list[ArgumentModel]) -> None:
        self._check_is_required_validator(config_argument, arguments)

    def _check_is_required_validator(self, config_argument: ArgumentConfigModel, arguments: list[ArgumentModel]) -> None:
        if config_argument.is_required == False:
            return
        for argument in arguments:
            if argument.name == config_argument.name and argument.type == "argument":
                return
            if argument.name == config_argument.alias and argument.type == "alias":
                return
        Store.are_arguments_correct = False
        error = f'Parameter "{config_argument.name}" is required for entity "entity" but was not provided.'
        print(error)
