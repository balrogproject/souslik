from django.db import DEFAULT_DB_ALIAS
from django.db.backends.postgresql.base import DatabaseWrapper

from pgbackend.connection import PooledConnection
from pgbackend.ops import DatabaseOperations


class DatabaseWrapper(DatabaseWrapper):
    ops_class = DatabaseOperations

    def __init__(self, settings_dict, alias=DEFAULT_DB_ALIAS):
        super().__init__(settings_dict, alias)
        self.connection = PooledConnection(db=self)
        self.connection.start_pool()

    def get_new_connection(self, conn_params):
        raise NotImplementedError
        return PooledConnection(db=self)

    def make_debug_cursor(self, cursor):
        return cursor

    def make_cursor(self, cursor):
        return cursor
