import psycopg2

from db_data import host, dbname, user, password



def insert_db_fn(queries):
    # print(queries)
    try:
        conn = psycopg2.connect(        # DB Connect
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port="5432"
        )
        conn.autocommit = True

        cur = conn.cursor()             # Cursor

        for q in queries:
            cur.execute(q)
            # pass

        print('[INFO] Executing Success.')

    except Exception as _ex:
        print('[INFO] Error while working with Postgres', _ex)
    finally:
        if conn:
            cur.close()
            conn.close()

