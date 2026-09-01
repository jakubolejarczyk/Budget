from budget.model import ProgramConfigModel
from budget.logic import ExitLogic


class ProgramConfig:
    PROGRAM_CONFIG: dict[str, ProgramConfigModel] = {
        "exit": ProgramConfigModel(
            name="exit",
            logic=ExitLogic().run,
        )
    }
