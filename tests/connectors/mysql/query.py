"""
Tests for "query" logic of "MySQL" DB Connector class.
"""

# System Imports.
import unittest

# User Imports.
from config import mysql_config, sqlite_config
from src.connectors import MysqlDbConnector, PostgresqlDbConnector, SqliteDbConnector


class TestMysqlQuery(unittest.TestCase):
    """
    Tests "MySQL" DB Connector class query logic.
    """
    @classmethod
    def setUpClass(cls):
        # Run parent setup logic.
        super().setUpClass()
