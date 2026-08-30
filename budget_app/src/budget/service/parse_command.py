class ParseCommandService:
    pass
    # def parse(self, cmd: str) -> CmdParserModel:
    #     cmd_items: list[str] = cmd.split(" ")
    #     program: str = self._get_program(cmd_items)
    #     program_arguments: str = self._get_program_arguments(cmd_items)
    #     command: str = self._get_command(cmd_items)
    #     command_arguments = self._get_command_arguments(cmd_items)
    #     cmd_model: CmdParserModel = CmdParserModel(
    #         program,
    #         program_arguments,
    #         command,
    #         command_arguments
    #     )
    #     return cmd_model

    # def _get_program(self, cmd_items: list[str]) -> str:
    #     if len(cmd_items) == 0:
    #         return ""
    #     program = cmd_items[0]
    #     if self._is_arg(program):
    #         return ""
    #     return program

    # def _get_program_arguments(self, cmd_items: list[str]) -> dict[str, dict[str, str | list[str]]]:
    #     arguments: dict[str, str] = {}
    #     if len(cmd_items) <= 1:
    #         return {}
    #     for cmd_item in cmd_items[1:]:
    #         if self._is_arg(cmd_item):
    #             argument: dict[str, str] = self._create_argument_alias(
    #                 cmd_item)
    #             arguments = arguments | argument
    #         else:
    #             break
    #     return arguments

    # def _get_command(self, cmd_items: list[str]) -> str:
    #     if len(cmd_items) <= 1:
    #         return ""
    #     for cmd_item in cmd_items[1:]:
    #         if self._is_arg(cmd_item):
    #             continue
    #         return cmd_item
    #     return ""

    # def _get_command_arguments(self, cmd_items: list[str]) -> dict[str, dict[str, str | list[str]]]:
    #     arguments: dict[str, str] = {}
    #     if len(cmd_items) <= 1:
    #         return {}
    #     start_index = 0
    #     for cmd_item in cmd_items:
    #         if start_index == 0:
    #             start_index += 1
    #             continue
    #         start_index += 1
    #         if not self._is_arg(cmd_item):
    #             break
    #     for cmd_item in cmd_items[start_index:]:
    #         if self._is_arg(cmd_item):
    #             argument: dict[str, str] = self._create_argument_alias(
    #                 cmd_item)
    #             arguments = arguments | argument
    #     return arguments

    # def _is_arg(self, cmd_item: str) -> bool:
    #     if cmd_item.startswith("-") or cmd_item.startswith("--"):
    #         return True
    #     return False

    # # The logic parses argument or alias from string to dictionary form
    # def _create_argument_alias(self, cmd_item: str) -> dict[str, dict[str, str | list[str]]]:
    #     argument_alias = cmd_item.strip().replace("--", "").replace("-", "")
    #     name: str
    #     value: str
    #     type: str
    #     if "=" in argument_alias:
    #         argument_alias_list = argument_alias.split("=")
    #         name = argument_alias_list[0]
    #         value = argument_alias_list[1]
    #         if "," in value:
    #             value = value.split(",")
    #     else:
    #         name = argument_alias
    #         value = ""
    #     if len(name) == 1:
    #         type = "alias"
    #     else:
    #         type = "argument"
    #     return {name: {"name": name, "value": value, "type": type}}
