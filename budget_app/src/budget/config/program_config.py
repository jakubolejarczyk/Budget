from budget.model import ProgramConfigModel, ArgumentConfigModel, CommandConfigModel
from budget.logic.budgets.budgets_logic import BudgetsLogic


class ProgramConfig:
    PROGRAM_CONFIG: list[ProgramConfigModel] = [
        ProgramConfigModel(
            name="budget",
            arguments=[],
            logic=BudgetsLogic().run,
            commands=[
                CommandConfigModel(
                    name="create",
                    arguments=[
                        ArgumentConfigModel(
                            name="month",
                            alias="m",
                            type="int",
                            default_value=None,
                            can_have_value=True,
                            can_have_multiple_values=False,
                            is_required=True
                        ),
                        ArgumentConfigModel(
                            name="year",
                            alias="y",
                            type="int",
                            default_value=None,
                            can_have_value=True,
                            can_have_multiple_values=False,
                            is_required=True
                        ),
                        ArgumentConfigModel(
                            name="amount",
                            alias="a",
                            type="float",
                            default_value=None,
                            can_have_value=True,
                            can_have_multiple_values=False,
                            is_required=True
                        )
                    ]
                )
            ]
        ),
        ProgramConfigModel(
            name="exit",
            logic=BudgetsLogic().run,
            arguments=[],
            commands=[]
        )
    ]
