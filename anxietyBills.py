import fn
from create_tables import create_connection
import argparse
import sys


def main(connection, executor):
    while True:
        print("1) Insert a new transaction")
        print("2) View transactions")
        print("3) View balance")
        print("4) Delete transactions")
        print("5) Insert transactions from csv")
        print("q) Exit")
        rep = input("-->")
        if rep == "1":
            fn.insert_transaction(executor, connection)
        elif rep == "2":
            print("(ID, DATE, AMOUNT, DESCRIPTION)")
            rows = fn.select_all(executor)
            for row in rows:
                print(row)
        elif rep == "3":
            print(fn.balance(executor))
        elif rep == "4":
            print("Witch transactions to delete ?\n eg. ---> 21,2,3,8")
            rows = fn.select_all(executor)
            for row in rows:
                print(row)
            rows = [int(x) for x in input().split(',')]
            fn.delete_transaction(rows, executor)
        elif rep == "5":
            file = input("Input file name\n--->")
            fn.file_insertion(executor, file)
            connection.commit()
        elif rep == "q":
            print("DON'T PANIC")
            break
        else:
            print("Wrong input")
            print("DON'T PANIC")
            connection.close()
            break


if __name__ == '__main__':
    conn = create_connection(r"C:\sqlite\db\anxiety_db.db")
    exe = conn.cursor()
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--insert", help="Insert a transaction\nanxietyBills -i yyyy-mm-dd,amount,description",
                        required=False)
    parser.add_argument("-fi", "--fileinsertion", help="Insert transactions from a file\nanxietyBills -fi path",
                        required=False)
    parser.add_argument("-b", "--balance", help="See the money balance\nanxietyBills -b", required=False,
                        action='store_true')
    parser.add_argument("-v", "--view", help="View all transactions", required=False, action='store_true')
    args = parser.parse_args()
    if args.insert:
        transaction = args.insert.split(',')
        if fn.date_check(transaction[0]) and fn.amount_check(transaction[1]) and len(transaction) == 3:
            fn.insert_into_transactions(exe, transaction[0], float(transaction[1]), transaction[2])
            conn.commit()
            sys.exit()
        else:
            print("Wrong transaction input")
            sys.exit()
    elif args.fileinsertion:
        fn.file_insertion(exe, args.fileinsertion)
        conn.commit()
        sys.exit()
    elif args.view:
        print("(ID, DATE, AMOUNT, DESCRIPTION)")
        rs = fn.select_all(exe)
        for r in rs:
            print(r)
        sys.exit()
    elif args.balance:
        print("The Balance:")
        print(fn.balance(exe))
        sys.exit()
    print(args)
    main(conn, exe)
