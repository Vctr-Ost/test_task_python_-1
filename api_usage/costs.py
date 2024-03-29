from insert_in_postgres import insert_db_fn
from get_requests import get_request
from queries_maker import queries_maker
from data_transformer import parse_csv


def costs_fn(prms):

    prms['dimensions'] = "location,channel,medium,campaign,keyword,ad_content,ad_group,landing_page"

    response = get_request('costs', prms).text
    json_rec = parse_csv(response, '	')
    queries = queries_maker('costs', json_rec)
    insert_db_fn(queries)

    print('[INFO] UPDATE COSTS SUCCESSFULL')
