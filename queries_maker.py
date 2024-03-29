from check_data_type import check_type
from data_transformer import get_nested


def queries_maker(tbl_name, json_rec):
    queries = []

    for doc in json_rec:
        if len(doc) <= 1:
            continue
        doc = get_nested(doc)
        query = single_query_maker(tbl_name, doc)
        queries.append(query)
    
    return queries


def single_query_maker(tbl_name, doc):

    ks = ", ".join(list(doc.keys())).replace('.', '_')
    vls = ""

    for k in doc.keys():

        if doc[k] is None:
                doc[k] = 'null'

        if k[-5:] == '_time' and check_type(doc[k]) == 'int':
            vls += f'TO_TIMESTAMP({doc[k]}/1000.0)'
        
        elif k[-5:] == '_time' and check_type(doc[k]) == 'str':
             vls += f'''TO_TIMESTAMP('{doc[k]}', 'YYYY-MM-DDTHH24:MI:SS.US')'''

        elif check_type(doc[k]) == 'int' or check_type(doc[k]) == 'float':
            vls += f'{doc[k]}'
        else:
            vls += f'\'{doc[k]}\''
        
        vls += ', '
    
    vls = vls[:-2]
    vls = null_finder(vls)

    query = f'INSERT INTO {tbl_name} ({ks}) VALUES ({vls});'

    return query


def null_finder(str):
    str = str.replace("'null'", 'null').replace("'Null'", 'null').replace("'None'", 'null').replace("'Undefined'", 'null').replace("''", 'null').replace("''", 'null')
    return str
