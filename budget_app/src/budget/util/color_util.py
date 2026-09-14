from enum import Enum


class ConsoleColor(Enum):
    PURPLE = "\033[36m"
    GRAY = "\033[90m"
    RED = "\033[91m"
    RESET = "\033[0m"


class ColorUtil:
    color: ConsoleColor = ConsoleColor.RESET

    @classmethod
    def set_color(cls, color: ConsoleColor) -> None:
        cls.color = color
        print(color.value, end="")
