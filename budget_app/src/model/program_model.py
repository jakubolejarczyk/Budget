from dataclasses import dataclass
from collections.abc import Callable
from .command_model import CommandModel


@dataclass
class ProgramModel:
    program: str
    command: dict[str, CommandModel]
    arguments: str
    method: Callable[[str], str]
