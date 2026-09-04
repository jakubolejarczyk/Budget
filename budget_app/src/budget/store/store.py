from mssql_python import Cursor


class Store:
    server: str
    database: str
    encrypt: str
    trusted_connection: str
    trust_server_certificate: str
    connection_string: str
    cursor: Cursor
    is_running: bool
    command: str
