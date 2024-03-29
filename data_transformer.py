import json
import pyarrow.parquet as pq
from io import BytesIO


def json_loads_get_json(str, param):
    json_file = json.loads(str)
    json_rec = json.loads(json_file.get(param))
    return json_rec


def json_loads_get_str(str, param):
    json_file = json.loads(str)
    res = json_file.get(param)
    return res


def parse_parquet_file(file):
    data = BytesIO(file)
    table = pq.read_table(data)
    df = table.to_pandas()
    res = df.to_dict(orient='records')
    return res


def parse_csv(str, delimiter):
    keys = str.split('\n')[0].split(delimiter)
    res = []

    for i in range( 1, len(str.split('\n')) ):
        values = str.split('\n')[i].split(delimiter)
        r_dict = dict(zip(keys, values))
        res.append(r_dict)

    return list(filter(None, res))


def get_nested(doc):
    res = {}
    for n in doc.keys():
        if type(doc[n]) == dict:
            for k in doc[n].keys():
                res[f'{n}_{k}'] = str(doc[n][k])
        else:
            res[n] = str(doc[n])

    return res
