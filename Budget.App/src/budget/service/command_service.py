from util import ColorUtil, LoggerUtil, ListUtil

class CommandService:
    def get_command(self):
        ColorUtil.set_color("cyan")
        command = input("Enter command: ")
        ColorUtil.reset_color()
        return command

    def parse_command(self, command):
        command_items = command.split()
        command_arguments = command_items[2:]
        command_data = {
            "program": ListUtil.get_list_element_by_index(command_items, 0),
            "command": ListUtil.get_list_element_by_index(command_items, 1),
            "arguments": [
                self._parse_command_argument(command_argument)
                for command_argument in command_arguments
            ]
        }
        return command_data

    def _parse_command_argument(self, command_argument):
        if "=" in command_argument:
            argument_items = command_argument.split("=")
            argument_data = {
                "argument": ListUtil.get_list_element_by_index(argument_items, 0),
                "value": ListUtil.get_list_element_by_index(argument_items, 1)
            }
            return argument_data
        else:
            argument_data = {
                "argument": command_argument,
                "value": None
            }
            return argument_data