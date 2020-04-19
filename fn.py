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


def select_all(executor):
    select_all_sql = """
                     SELECT date, amount, description
                     FROM transactions
                     """
    return executor.execute(select_all_sql)
