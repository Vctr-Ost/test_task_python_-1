from insert_in_postgres import insert_db_fn
from get_requests import get_request
from queries_maker import queries_maker
from data_transformer import json_loads_get_json


def installs_fn(prms):

    response = get_request('installs', prms).text
    json_rec = json_loads_get_json(response, 'records')
    queries = queries_maker('installs', json_rec)
    insert_db_fn(queries)
    print('[INFO] UPDATE INSTALLS SUCCESSFULL')
