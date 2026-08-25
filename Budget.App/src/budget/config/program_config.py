from model import ProgramModel

class ProgramConfig:
    def __init__(self):
        self.config = []
        self.config.append(ProgramModel({
            "program": "exit",
            "command": None,
            "arguments": []
        }))