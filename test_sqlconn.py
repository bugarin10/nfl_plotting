import unittest
from unittest.mock import patch

from sqlconn import sqlConnect

class TestSQLConnect(unittest.TestCase):

    @patch('databricks.sql.connect')
    def test_sqlConnect_successful(self, mock_connect):
        # Test a successful connection
        mock_connect.return_value.cursor.return_value = 'mock_cursor'
        result = sqlConnect()
        self.assertEqual(result[0], 'mock_cursor')

if __name__ == '__main__':
    unittest.main()