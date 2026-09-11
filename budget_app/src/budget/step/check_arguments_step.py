from budget.model import ArgumentModel, ProgramConfigModel, CommandConfigModel, ArgumentConfigModel
from budget.store import Store
from budget.util import ParseUtil


class CheckArgumentsStep:
    def run(self, config: ProgramConfigModel | CommandConfigModel, arguments: list[ArgumentModel]) -> None:
        Store.are_arguments_correct = True
        config_arguments: list[ArgumentConfigModel] = []
        if config:
            config_arguments = config.arguments
        for config_argument in config_arguments:
            self._check_argument(config, config_argument, arguments)

    def _check_argument(self, config: ProgramConfigModel | CommandConfigModel, config_argument: ArgumentConfigModel, arguments: list[ArgumentModel]) -> None:
        self._check_is_required_validator(config, config_argument, arguments)
        self._check_can_have_value(config, config_argument, arguments)
        self._check_can_have_multiple_values(
            config, config_argument, arguments
        )
        self._check_type(config, config_argument, arguments)

    def _check_is_required_validator(self, config: ProgramConfigModel | CommandConfigModel, config_argument: ArgumentConfigModel, arguments: list[ArgumentModel]) -> None:
        if config_argument.is_required == False:
            return
        for argument in arguments:
            if argument.name == config_argument.name and argument.type == "argument":
                return
            if argument.name == config_argument.alias and argument.type == "alias":
                return
        Store.are_arguments_correct = False
        error = f'Parameter "{config_argument.name}" is required for entity "{config.name}" but was not provided.'
        print(error)

    def _check_can_have_value(self, config: ProgramConfigModel | CommandConfigModel, config_argument: ArgumentConfigModel, arguments: list[ArgumentModel]) -> None:
        if config_argument.can_have_value == True:
            return
        current_argument: ArgumentModel = None
        for argument in arguments:
            if argument.name == config_argument.name and argument.type == "argument":
                current_argument = argument
                break
            if argument.name == config_argument.alias and argument.type == "alias":
                current_argument = argument
                break
        if current_argument is None:
            return
        if current_argument.value == None:
            return
        Store.are_arguments_correct = False
        error = f'Parameter "{config_argument.name}" has value for entity "{config.name}" but is not permitted.'
        print(error)

    def _check_can_have_multiple_values(self, config: ProgramConfigModel | CommandConfigModel, config_argument: ArgumentConfigModel, arguments: list[ArgumentModel]) -> None:
        if config_argument.can_have_multiple_values == True:
            return
        current_argument: ArgumentModel = None
        for argument in arguments:
            if argument.name == config_argument.name and argument.type == "argument":
                current_argument = argument
                break
            if argument.name == config_argument.alias and argument.type == "alias":
                current_argument = argument
                break
        if current_argument is None:
            return
        if type(current_argument.value) is not list:
            return
        Store.are_arguments_correct = False
        error = f'Parameter "{config_argument.name}" has multiple values for entity "{config.name}" but is not permitted.'
        print(error)

    def _check_type(self, config: ProgramConfigModel | CommandConfigModel, config_argument: ArgumentConfigModel, arguments: list[ArgumentModel]) -> None:
        current_argument: ArgumentModel = None
        for argument in arguments:
            if argument.name == config_argument.name and argument.type == "argument":
                current_argument = argument
                break
            if argument.name == config_argument.alias and argument.type == "alias":
                current_argument = argument
                break
        if current_argument is None:
            return
        if config_argument.type == "str" and type(current_argument.value) == "str":
            return
        if config_argument.type == "int" and ParseUtil.try_parse_int(current_argument.value):
            return
        if config_argument.type == "float" and ParseUtil.try_parse_float(current_argument.value):
            return
        Store.are_arguments_correct = False
        error = f'Parameter "{config_argument.name}" must be {config_argument.type} type for entity "{config.name}" but is not.'
        print(error)
