from dataclasses import dataclass
from collections.abc import Callable
from .program_model import ArgumentModel


@dataclass
class ProgramConfigModel:
    name: str
    logic: Callable[[str, list[ArgumentModel]], None]
