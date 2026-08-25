from service import CommandService

class BudgetApp:
    def __init__(self):
        self.commandService = CommandService()

    def run(self):
        while True:
            command = self.commandService.get_command()
            command_data = self.commandService.parse_command(command)
            print(command_data)