import requests
import json

from insert_in_postgres import insert_db_fn
from db_data import authKey, apiUrl


def installs_fn(prms):          # prms = {"date": "2024-03-26"}

    r = requests.get(f'{apiUrl}/installs', params=prms, headers=authKey)

    json_file = json.loads(r.text)
    json_rec = json.loads(json_file['records'])
    
    queries = []

    for doc in json_rec:    # list with dicts
        ks = ", ".join(list(doc.keys()))
        vls = ""

        for k in doc.keys():
            if doc[k] is None:
                doc[k] = 'null'
                
            if k == 'install_time':
                vls += f'''TO_TIMESTAMP('{doc[k]}', 'YYYY-MM-DDTHH24:MI:SS.US')'''
            else:
                vls += f'\'{doc[k]}\''
        
            if k != 'official_name':
                vls += ', '

        vls = vls.replace("'null'", 'null').replace("'None'", 'null').replace("'Undefined'", 'null').replace('\n', '').replace(' ', '')
        queries.append(f'INSERT INTO installs ({ks}) VALUES ({vls});')
    
    insert_db_fn(queries)

    print('[INFO] UPDATE INSTALLS SUCCESSFULL')
