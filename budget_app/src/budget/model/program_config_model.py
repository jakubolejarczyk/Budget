from dataclasses import dataclass
from collections.abc import Callable
from .program_model import ProgramModel


@dataclass
class ProgramConfigModel:
    name: str
    logic: Callable[[ProgramModel], None]
