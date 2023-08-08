import psycopg2


class ConnectDataBase:
    def __init__(self):
        self._connect = psycopg2.connect(
            host="localhost",
            database="DBSistemaMercado",
            user="postgres",
            password="12345"
        )

    def get_cursor(self):
        self._connect.get_dsn_parameters()
        return self._connect.cursor()

    def commit(self):
        self._connect.commit()

