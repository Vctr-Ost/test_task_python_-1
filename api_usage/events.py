import json
from insert_in_postgres import insert_db_fn
from get_requests import get_request
from queries_maker import queries_maker
from data_transformer import json_loads_get_json, json_loads_get_str


def events_fn(prms):
    
    next_page_str = get_req(prms)

    if next_page_str is not None:
        prms['next_page'] = next_page_str
        events_fn(prms)
    else:
        print(f'[INFO] UPDATE EVENTS SUCCESSFULL')


def get_req(prms):

    try:
        response = get_request('events', prms).text
        next_page_str = json_loads_get_str(response, 'next_page')
        data = json_loads_get_json(response, 'data')
        queries = queries_maker('events', data)
        insert_db_fn(queries)
        return next_page_str

    except json.JSONDecodeError as e:
        print('Error decoding JSON:', e)
        return get_req(prms)
