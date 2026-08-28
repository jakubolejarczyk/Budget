class GetInputService:
    def get_input(self) -> str:
        return self._get_input_from_keyboard()

    def _get_input_from_keyboard(self) -> str:
        return input("> ")
