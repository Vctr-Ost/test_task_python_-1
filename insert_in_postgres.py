import psycopg2
from dotenv import load_dotenv
import os


def insert_db_fn(queries):
    
    try:
        load_dotenv()

        conn = psycopg2.connect(        # DB Connect
            dbname=os.getenv("dbname"),
            user=os.getenv("user"),
            password=os.getenv("password"),
            host=os.getenv("host"),
            port=os.getenv("port")
        )

        conn.autocommit = True
        cur = conn.cursor()             # Cursor

        for q in queries:
            cur.execute(q)

        print('[INFO] Inserting Success.')

    except Exception as _ex:
        print('[ERROR] Error while working with Postgres\n', _ex)
    finally:
        if conn:
            cur.close()
            conn.close()

