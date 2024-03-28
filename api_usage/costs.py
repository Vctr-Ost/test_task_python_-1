import requests

from insert_in_postgres import insert_db_fn
from db_data import authKey, apiUrl


def costs_fn(prms):          # prms = {"date": "2024-03-26"}

    prms['dimensions'] = "location,channel,medium,campaign,keyword,ad_content,ad_group,landing_page"

    r = requests.get(f'{apiUrl}/costs', params=prms, headers=authKey)

    keys = r.text.split('\n')[0].split()

    json_rec = []

    for i in range( 1, len(r.text.split('\n')) ):
        values = r.text.split('\n')[i].split('	')
        r_dict = dict(zip(keys, values))
        json_rec.append(r_dict)
    
    json_rec = list(filter(None, json_rec))
    
    queries = []

    # print(json_rec)

    for doc in json_rec:    # list with dicts
        if len(doc) < 2:
            continue
        
        ks = ", ".join(list(doc.keys()))
        vls = ""            

        for k in doc.keys():
            if doc[k] is None:
                doc[k] = 'null'
                
            if k == 'cost':
                vls += f'{doc[k]}'
            else:
                vls += f'\'{doc[k]}\''
                
            if k != 'cost':
                vls += ', '

        vls = vls.replace("'null'", 'null').replace("'None'", 'null').replace("'Undefined'", 'null').replace('\n', '')
        
        # filtered_list = [d for d in list_of_dicts if len(d) > 1]
        # print(ks)
        # print(vls)
        
        queries.append(f'INSERT INTO costs ({ks}) VALUES ({vls});')
    
    insert_db_fn(queries)

    print('[INFO] UPDATE COSTS SUCCESSFULL')























# import requests
# import json
# import psycopg2

# from db_data import authKey, apiUrl, host, dbname, user, password


# def costs_fn(prms):          # prms = {"date": "2024-03-26"}

#     prms['dimensions'] = "location,channel,medium,campaign,keyword,ad_content,ad_group,landing_page"

#     r = requests.get(f'{apiUrl}/costs', params=prms, headers=authKey)

#     # json_file = json.loads(r.text)
#     # json_rec = json.loads(json_file['records'])

#     keys = r.text.split('\n')[0].split()

#     json_rec = []

#     for i in range( 1, len(r.text.split('\n')) ):
#         values = r.text.split('\n')[i].split()
#         r_dict = dict(zip(keys, values))
#         json_rec.append(r_dict)
    
#     json_rec = list(filter(None, json_rec))
    
#     # print(json_rec)
#     # print(type(json_rec))
#     # print(json_rec[0:3])

#     try:
#         conn = psycopg2.connect(        # DB Connect
#             dbname=dbname,
#             user=user,
#             password=password,
#             host=host,
#             port="5432"
#         )
#         conn.autocommit = True

#         cur = conn.cursor()             # Cursor 

#         for doc in json_rec:    # list with dicts
#             ks = ", ".join(list(doc.keys()))
#             vls = ""

#             for k in doc.keys():
#                 if doc[k] is None:
#                     doc[k] = 'null'
                
#                 if k == 'install_time':
#                     vls += f'''TO_TIMESTAMP('{doc[k]}', 'YYYY-MM-DDTHH24:MI:SS.US')'''
#                 else:
#                     vls += f'\'{doc[k]}\''
                
#                 if k != 'cost':
#                     vls += ', '

#             vls = vls.replace("'null'", 'null').replace("'None'", 'null').replace("'Undefined'", 'null').replace('\n', '').replace(' ', '')
#             cur.execute(f'INSERT INTO costs ({ks}) VALUES ({vls});')

#         print('[INFO] Executing Success.')

#     except Exception as _ex:
#         print('[INFO] Error while working with Postgres', _ex)
#     finally:
#         if conn:
#             cur.close()
#             conn.close()
