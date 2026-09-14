from collections.abc import Callable
from dataclasses import dataclass
from .argument_config_model import ArgumentConfigModel
from .command_config_model import CommandConfigModel


@dataclass
class ProgramConfigModel:
    name: str
    logic: Callable[[str], str]
    arguments: list[ArgumentConfigModel]
    commands: list[CommandConfigModel]
