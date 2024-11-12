# utils/db.py
import sqlite3

DATABASE_PATH = "patient_tracking.db"  # Correct database path

def get_db_connection():
    '''Create and return a connection and cursor to the database.'''
    CONN = sqlite3.connect(DATABASE_PATH)  # Use the correct database file
    CONN.row_factory = sqlite3.Row  # This helps to access columns by name
    CURSOR = CONN.cursor()  # Use CURSOR in uppercase
    return CONN, CURSOR