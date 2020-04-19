import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn


def create_table(connection, create_table_sql):
    """create a certain sql table via the given connection"""
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)


def main():
    database = r"C:\sqlite\db\anxiety_db.db"
    create_table_transactions = """ CREATE TABLE IF NOT EXISTS transactions(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    date text NOT NULL,
                                    amount double(10,2) NOT NULL,
                                    description text NOT NULL
                                    );
                                    """
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, create_table_transactions)
    else:
        print("Error! Can not crate the database connection")


if __name__ == '__main__':
    main()
