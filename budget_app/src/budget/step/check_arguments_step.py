from budget.model import ArgumentModel, ProgramConfigModel, CommandConfigModel, ArgumentConfigModel
from budget.store import Store


class CheckArgumentsStep:
    def run(self, arguments: list[ArgumentModel], config: ProgramConfigModel | CommandConfigModel) -> None:
        Store.are_arguments_correct = True
        config_arguments: list[ArgumentConfigModel] = []
        if config:
            config_arguments = config.arguments
        for config_argument in config_arguments:
            self._check_is_required(config_argument, arguments)

    def _check_is_required(self, config_argument: ArgumentConfigModel, arguments: list[ArgumentModel]) -> None:
        for argument in arguments:
            if argument.name == config_argument.name and argument.type == "argument":
                return
            elif argument.name == config_argument.alias and argument.type == "alias":
                return
        Store.are_arguments_correct = False
        error = f'Parameter "{config_argument.name}" is required but was not provided.'
        print(error)
