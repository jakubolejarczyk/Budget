from dataclasses import dataclass
from .argument_model import ArgumentModel


@dataclass
class CommandModel:
    name: str
    arguments: list[ArgumentModel]
