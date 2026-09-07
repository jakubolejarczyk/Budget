from dataclasses import dataclass
from .argument_config_model import ArgumentConfigModel


@dataclass
class CommandConfigModel:
    name: str
    arguments: list[ArgumentConfigModel]
