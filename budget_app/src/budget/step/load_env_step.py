from dotenv import load_dotenv


class LoadEnvStep:
    def run(self) -> None:
        load_dotenv()
