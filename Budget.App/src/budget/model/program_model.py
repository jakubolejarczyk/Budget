class ProgramModel:
    def __init__(self, data):
        self._program = data["program"]
        self._command = data["command"]
        self._arguments = data["arguments"]

    def get_program(self):
        return self._program

    def get_command(self):
        return self._command

    def get_arguments(self):
        return self._arguments