from dataclasses import dataclass
from typing import Union
import psycopg


@dataclass
class SqlConfig:
    host: str
    port: int
    user: Union[str, None]
    password: Union[str, None]
    db: str

class SqlClient:
    def __init__(self, sql_config: SqlConfig) -> None:
        # Connection info
        self.host = sql_config.host
        self.port = sql_config.port
        self.address = f'{self.host}:{self.port}'
        self.user = sql_config.user
        self.password = sql_config.password
        self.db = sql_config.db
        # Psycopg
        self.conn = Union[psycopg.Connection, None]
    
    def try_connect(self) -> psycopg.cursor:
        """Creates a connection and a cursor to manage the DB.
        """
        try:
            # Test if connection is open
            cursor = self.conn.cursor()
            cursor.execute("SELECT version()")
            print(f'Already connected to {self.host}')

        except Exception as e:
            print(f'Connecting to {self.host}...')

            self.conn = psycopg.connect(
                dbname=self.db,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )

    def select_data(self, query: str) -> list:
        """Get last data from the specified table.
        """
        # Result
        rows = []

        # Get connection
        self.try_connect()

        # Execute SQL query
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            # Fetch results
            rows = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print(e)

        return rows
    
    def insert_data(self, query: str) -> None:
        """Insert data to the specified table.
        """
        self.try_connect()

        # Execute SQL queries
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        cursor.close()

    def close(self):
        """Close connection
        """
        self.conn.close()

if __name__ == '__main__':
    config = SqlConfig(
        host='localhost',
        port=5432,
        user='postgres',
        password='myPassword',
        db='mydb',
    )

    client = SqlClient(sql_config=config)
    rows = client.select_data(f'SELECT * FROM words ORDER BY datetimecolumn DESC LIMIT 1')
    client.close()

    print(rows)
