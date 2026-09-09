from budget.store import Store


class TerminateStoreStep:
    def run(self) -> None:
        Store.server = None
        Store.database = None
        Store.encrypt = None
        Store.trusted_connection = None
        Store.trust_server_certificate = None
        Store.connection_string = None
        Store.cursor = None
        Store.is_running = False
        Store.command = None
        Store.program = None
        Store.selected_program_config = None
        Store.selected_command_config = None
        Store.are_arguments_correct = True
