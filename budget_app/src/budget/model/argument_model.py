from dataclasses import dataclass


@dataclass
class ArgumentModel:
    name: str
    value: str | list[str] | None
    has_value: bool
    has_multiple_values: bool
    type: str
