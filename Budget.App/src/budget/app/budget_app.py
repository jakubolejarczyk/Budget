from service.command_service import CommandService

class BudgetApp:
    def __init__(self):
        self.commandService = CommandService()

    def run(self):
        while True:
             command = input("> ")
             self.commandService.run_command(command)