from dataclasses import dataclass


@dataclass
class CmdParserModel:
    program: str
    program_arguments: dict[str, str]
    command: str
    command_arguments: dict[str, str]
