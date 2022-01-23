"""
Tests for "display" logic of "Core" DB Connector class.
"""

# System Imports.
import unittest

# User Imports.
from config import mysql_config, sqlite_config
from src.connectors import MySqlConnector, SqliteConnector


class TestCoreDisplay(unittest.TestCase):
    """
    Tests "Core" DB Connector class display logic.
    """
    @classmethod
    def setUpClass(cls):
        # Run parent setup logic.
        super().setUpClass()
