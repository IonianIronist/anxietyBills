import re
import csv

def insert_into_transactions(executor, date, amount, description):
    insert_into_sql = f"""
                      INSERT INTO transactions (date, amount, description)
                      VALUES(
                        '{date}',
                        {amount},
                        '{description}'
                      );
                      """
    executor.execute(insert_into_sql)


def delete_transaction(transactions, executor):
    for transaction in transactions:
        executor.execute(f"DELETE FROM transactions WHERE transactions.id == {transaction}")


def date_check(date):
    rexp = re.compile(r"[0-9]{4}(-[0-9]{2}){2}")
    if rexp.match(date) is not None:
        return date
    else:
        return None


def amount_check(amount):
    rexp = re.compile(r"-?[0-9]+\.[0-9]{2}")
    if rexp.match(rep) is not None:
        return amount
    else:
        return None


def select_all(executor):
    select_all_sql = """SELECT * FROM transactions"""
    return executor.execute(select_all_sql).fetchall()


def insert_transaction(executor, connection):
    while True:
        print("Input date yyyy-mm-dd")
        rep = input("-->")
        rexp = re.compile(r"[0-9]{4}(-[0-9]{2}){2}")
        if date_check(rep) is not None:
            date = date_check(rep)
            break
        else:
            print("Wrong type input")

    while True:
        print("Input amount spent/received\nfor info input '-h'")
        rep = input("-->")
        if rep == r"-h":
            print(
                """If you want to declare a negative transaction the
                input should be
                -(amount)
                a positive transaction should be just (amount)
                The amount should always be followed by two float digits
                i.e. 1234.56 """)
            rep = input("-->")
        if amount_check(rep) is not None:
            amount = amount_check(rep)
            break
        else:
            print("Wrong type input")

    print("Input a description of the transaction")
    description = input("-->")
    insert_into_transactions(executor, date, amount, description)
    connection.commit()


def file_insertion(executor, file):
    with open(file, 'r') as filename:
        reader = csv.reader(filename)
        for row in reader:
            date, amount, description = row[0], float(row[1]), row[2]
            insert_into_transactions(executor, date, amount, description)


def balance(executor):
    rows = select_all(executor)
    return sum(i[2] for i in rows)
