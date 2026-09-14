from budget.store import Store
from budget.util import ColorUtil, ConsoleColor


class FetchCommandStep:
    def run(self) -> None:
        ColorUtil.set_color(ConsoleColor.PURPLE)
        Store.command = self._fetch_input()
        ColorUtil.set_color(ConsoleColor.RESET)

    def _fetch_input(self) -> str:
        return input("Enter command: ")
