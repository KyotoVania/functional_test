import pytest
import sys
from os.path import abspath, dirname
import sqlite3

sys.path.insert(0, abspath(dirname(dirname(__file__))))

# Now you can import the Calculator class
# Add your test cases here
# tests/test_exercice3.py

from math import pi
from exercice4 import DatabaseManager


def test_database_manager():
    # Create an in-memory database
    db_manager = DatabaseManager(':memory:')
    
    # Create a table
    columns = {'id': 'INTEGER', 'name': 'TEXT', 'age': 'INTEGER'}
    db_manager.create_table('students', columns)
    
    # Insert data into the table
    data = {'id': 1, 'name': 'John', 'age': 25}
    db_manager.insert_into_table('students', data)
    
    # Select data from the table
    result = db_manager.select_from_table('students')
    assert result == [(1, 'John', 25)]
    
    # Update data in the table
    updated_data = {'age': 26}
    condition = 'id = 1'
    db_manager.update_table('students', updated_data, condition)
    
    # Select updated data from the table
    result = db_manager.select_from_table('students')
    assert result == [(1, 'John', 26)]
    
    # Delete data from the table
    condition = 'id = 1'
    db_manager.delete_from_table('students', condition)
    
    # Select data after deletion
    result = db_manager.select_from_table('students')
    assert result == []
    
    # Close the connection
    db_manager.close_connection()