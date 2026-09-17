import sqlite3


DATABASE = "portscan.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT NOT NULL,
            start_port INTEGER NOT NULL,
            end_port INTEGER NOT NULL,
            scan_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS scan_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            scan_id INTEGER NOT NULL,
            port INTEGER NOT NULL,
            service TEXT,
            risk TEXT,
            description TEXT,
            FOREIGN KEY (scan_id) REFERENCES scans(id)
        )
    """)

    connection.commit()
    connection.close()