import mysql.connector

from typing import Union, Tuple, List

SQLQueryParameter = Union[List, Tuple, List[Tuple], List[List], Tuple[Tuple], Tuple[List]]


class DatabaseClass:
    def __init__(self, config):
        self.host = config.host
        self.port = config.port
        self.user = config.user
        self.password = config.password
        self.database = config.database

        self.__connect_to_db()
        self.__get_cursor()

    def __connect_to_db(self):
        self.db = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
        )

    def __get_cursor(self):
        self.cursor = self.db.cursor(dictionary=True, buffered=True)

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def last_inserted_id(self):
        return self.cursor.lastrowid

    def query(self, query: str, params: SQLQueryParameter = None, commit=True):
        if params is None:
            self.cursor.execute(query)
        else:
            if isinstance(params[0], list) or isinstance(params[0], tuple):
                self.cursor.executemany(query, params)
            else:
                self.cursor.execute(query, params)
        if commit == True:
            self.db.commit()

    def query_to_array(self, query: str, params: SQLQueryParameter = None) -> list:
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def get_row(self, query: str, params: SQLQueryParameter = None) -> dict:
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.db.close()