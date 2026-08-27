from dataclasses import dataclass


@dataclass
class CmdParserModel:
    program: str
    program_args: dict[str, str]
    command: str
    command_args: dict[str, str]
