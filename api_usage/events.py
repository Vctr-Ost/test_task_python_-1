import requests
import json

from insert_in_postgres import insert_db_fn
from db_data import authKey, apiUrl

counter = 0

def events_fn(prms):          # prms = {"date": "2024-03-26"} + 
    global counter
    counter += 1
    next_page_str = get_req(prms)


    if next_page_str is not None:
        prms['next_page'] = next_page_str
        events_fn(prms)
    else:
        print(f'[INFO] UPDATE EVENTS SUCCESSFULL\n       Counter={counter}')


def get_req(prms):

    try:
        r = requests.get(f'{apiUrl}/events', params=prms, headers=authKey)
        json_file = json.loads(r.text)
        next_page_str = json_file.get('next_page')
        data = json.loads(json_file['data'])

        make_queries(data)

        return next_page_str

    except json.JSONDecodeError as e:
        print('Error decoding JSON:', e)
        return get_req(prms)


def make_queries(json_rec):
    queries = []

    for doc in json_rec:    # list with dicts

        for k in doc.keys():
            if type(doc[k]) != str and type(doc[k]) != dict:
                doc[k] = str(doc[k])

        for k in doc['user_params'].keys():
            if type(doc['user_params'][k]) != str:
                doc['user_params'][k] = str(doc['user_params'][k])

            doc[f'user_params_{k}'] = doc['user_params'][k]

        del doc['user_params']


        ks = ", ".join(list(doc.keys()))
        vls = ""

        for k in doc.keys():
            if k == 'event_time':
                vls += f'''TO_TIMESTAMP({doc[k]}/1000.0)'''
            elif check_type(doc[k]) == 'int' or check_type(doc[k]) == 'float':
                vls += f'{doc[k]}'
            else:
                vls += f'\'{doc[k]}\''
            
            vls += ', '

        vls = vls[:-2]
        vls = vls.replace("'null'", 'null').replace("'Null'", 'null').replace("''", 'null').replace("'None'", 'null').replace("'Undefined'", 'null')

        queries.append(f'INSERT INTO events ({ks}) VALUES ({vls});')

    
    insert_db_fn(queries)


def check_type(value):
    try:
        float_value = float(value)
        int_value = int(float_value)
        if int_value == float_value:
            return "int"
        else:
            return "float"
    except ValueError:
        return "str"