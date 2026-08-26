from dataclasses import dataclass
from collections.abc import Callable


@dataclass
class CommandModel:
    command: str
    arguments: str
    method: Callable[[str], str]
