class ParseUtil:
    @staticmethod
    def try_parse_int(value: str) -> bool:
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def try_parse_float(value: str) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False
