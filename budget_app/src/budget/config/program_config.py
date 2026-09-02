from budget.model import ProgramConfigModel
from budget.logic import ExitLogic, UnknownProgramLogic


class ProgramConfig:
    PROGRAM_CONFIG: dict[str, ProgramConfigModel] = {
        "exit": ProgramConfigModel(
            name="exit",
            logic=ExitLogic().run,
        ),
        "unknown_program": ProgramConfigModel(
            name="unknown_program",
            logic=UnknownProgramLogic().run,
        ),
    }
