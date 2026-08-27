from dataclasses import dataclass


@dataclass
class CmdParserModel:
    program: str
    program_arguments: dict[str, str | list[str]]
    command: str
    command_arguments: dict[str, str | list[str]]
