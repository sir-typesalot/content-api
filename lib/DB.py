import os
import logging
import pymysql.cursors
from dotenv import load_dotenv

logging.basicConfig(level = logging.INFO)

class Database(object):

    logger = logging.getLogger("db_logger")

    def __init__(self):
        load_dotenv()
        self.HOST = os.environ['HOST']
        self.USER = os.environ['USER']
        self.PASSWORD = os.environ['PASSWORD']

        self.config = {
            "host": self.HOST,
            "user": self.USER,
            "password": self.PASSWORD,
            "db": self.db
        }
        self._conn = pymysql.connect(**self.config)
        self._cursor = self._conn.cursor(dictionary=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            self._conn.commit()
        else:
            self._conn.rollback()
        self._conn.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self._conn.commit()

    def close(self, commit=True):
        if commit:
            self.commit()
        self._conn.close()

    def execute(self, sql, params=None):
        self._cursor.execute(sql, params or ())

    def fetchall(self):
        return self._cursor.fetchall()

    def fetchone(self):
        return self._cursor.fetchone()
