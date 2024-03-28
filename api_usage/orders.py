import requests
import json
import pandas as pd
import pyarrow.parquet as pq
from io import BytesIO

from insert_in_postgres import insert_db_fn
from db_data import authKey, apiUrl


def orders_fn(prms):          # prms = {"date": "2024-03-26"}
    r = requests.get(f'{apiUrl}/orders', params=prms, headers=authKey)
    data = BytesIO(r.content)
    table = pq.read_table(data)
    df = table.to_pandas()

    # print(df.head())
    json_rec = df.to_dict(orient='records')

    queries = []

    for doc in json_rec:
        for k in doc.keys():
            if type(doc[k]) != str:
                doc[k] = str(doc[k])

    # print(json_rec[0])
    # print('--------------------------------------------------------------------------------------------')

        ks = ", ".join(list(doc.keys())).replace('.', '_')
        vls = ""

        for k in doc.keys():
            if k == 'event_time':
                vls += f'\'{doc[k]}\''
            elif check_type(doc[k]) == 'int' or check_type(doc[k]) == 'float':
                vls += f'{doc[k]}'
            else:
                vls += f'\'{doc[k]}\''
            
            vls += ', '
        
        vls = vls[:-2]
        vls = vls.replace("'null'", 'null').replace("'Null'", 'null').replace("''", 'null').replace("'None'", 'null').replace("'Undefined'", 'null')

        queries.append(f'INSERT INTO orders ({ks}) VALUES ({vls});')
    
    insert_db_fn(queries)

    print('[INFO] UPDATE ORDERS SUCCESSFULL')


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