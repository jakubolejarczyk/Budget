from budget.model import ProgramConfigModel, CommandConfigModel, ArgumentConfigModel


class ProgramConfig:
    PROGRAM_CONFIG: list[ProgramConfigModel] = [
        ProgramConfigModel(
            name="budget",
            arguments=[],
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
            arguments=[],
            commands=[]
        )
    ]
