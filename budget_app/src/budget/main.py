from os import getenv
from dotenv import load_dotenv
from mssql_python import connect
from budget.app import BudgetApp


def main() -> None:
    load_dotenv()
    connection_string = getenv("SQL_CONNECTION_STRING")
    if connection_string is None:
        raise ValueError(
            "SQL_CONNECTION_STRING environment variable is not set.")
    connection = connect(connection_string)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    BudgetApp().run()


if __name__ == "__main__":
    main()
