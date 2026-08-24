from util import ColorUtil, LoggerUtil

class CommandService:
    def get_command(self):
        ColorUtil.set_color("cyan")
        command = input("Enter command: ")
        ColorUtil.reset_color()
        return command

    def run_command(self, command):
        ColorUtil.set_color("dark_gray")
        LoggerUtil.log_message(f"Your command is: {command}")
        ColorUtil.reset_color()