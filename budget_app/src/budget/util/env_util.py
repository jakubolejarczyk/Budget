from os import getenv


class EnvUtil:
    def get_env(key: str) -> str:
        return getenv(key)
