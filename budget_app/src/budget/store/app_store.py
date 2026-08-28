class AppStore:
    is_running: bool

    @staticmethod
    def init():
        AppStore.is_running = True

    @staticmethod
    def terminate():
        AppStore.is_running = False
