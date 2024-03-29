from insert_in_postgres import insert_db_fn
from get_requests import get_request
from queries_maker import queries_maker
from data_transformer import parse_parquet_file


def orders_fn(prms):

    response = get_request('orders', prms).content
    json_rec = parse_parquet_file(response)
    queries = queries_maker('orders', json_rec)
    insert_db_fn(queries)

    print('[INFO] UPDATE ORDERS SUCCESSFULL')
