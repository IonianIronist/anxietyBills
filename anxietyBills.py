import re
import sqlite3
from sqlite3 import Error

import fn
from create_tables import create_connection


def main(conn):
    executor = conn.cursor()
    while True:
        print("1) Insert a new transaction")
        print("2) View transactions")
        print("q) Exit")
        rep = input("-->")
        if rep is "1":
            while True:
                print("Input date yyyy-mm-dd")
                rep = input("-->")
                rexp = re.compile(r"[0-9]{4}(-[0-9]{2}){2}")
                if rexp.match(rep) is not None:
                    date = rep
                    break
                else:
                    print("Wrong type input")

            print("Input amount spent/recived\nfor info input '-h'")
            rep = input("-->")
            while True:
                if rep == r"-h":
                    print(
                        """If you want to declare a negative transaction the
                        input should be
                        -(amount)
                        a positive transaction should be just (amount)
                        The amount should always be followed by two float digits
                        i.e. 1234.56 """)
                    rep = input("-->")
                rexp = re.compile(r"-?[0-9]+\.[0-9]{2}")
                if rexp.match(rep) is not None:
                    amount = rep
                    break
                else:
                    print("Wrong type input")

            print("Input a description of the transaction")
            description = input("-->")
            fn.insert_into_transactions(executor, date, amount, description)
            conn.commit()
        elif rep is "2":
            tupples = fn.select_all(executor)
            rows = tupples.fetchall()
            for row in rows:
                print(row)
        elif rep is "q":
            print("DONT PANIC")
            break
        else:
            print("Wrong input")
            conn.close()
            break


if __name__ == '__main__':
    conn = create_connection(r"C:\sqlite\db\anxiety_db.db")
    main(conn)
