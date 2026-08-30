from dataclasses import dataclass
from .argument_model import ArgumentModel
from .command_model import CommandModel


@dataclass
class ProgramModel:
    name: str
    arguments: list[ArgumentModel]
    command: CommandModel
