from dataclasses import dataclass


@dataclass
class ArgumentConfigModel:
    name: str
    alias: str
    type: str
    default_value: str | None
    can_have_value: bool
    can_have_multiple_values: bool
    is_required: bool
