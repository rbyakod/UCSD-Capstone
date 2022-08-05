import json


def flattening(nested, prefix, ignore_list):
    field = {}

    flatten(True, nested, field, prefix, ignore_list)

    return field


def flatten(top, nested, flatdict, prefix, ignore_list):
    def assign(new_key, data, toignore):
        if toignore:
            if isinstance(data, (dict, list, tuple,)):
                json_data = json.dumps(data)
                flatdict[new_key] = json_data
            else:
                flatdict[new_key] = data
        else:
            if isinstance(data, (dict, list, tuple,)):
                flatten(False, data, flatdict, new_key, ignore_list)
            else:
                flatdict[new_key] = data

    if isinstance(nested, dict):
        for key, value in nested.items():
            ok = match_key(ignore_list, key)
            if ok and prefix == "":
                assign(key, value, True)
            elif ok and prefix != "":
                new_key = create_key(top, prefix, key)
                assign(new_key, value, True)
            else:
                new_key = create_key(top, prefix, key)
                assign(new_key, value, False)

    elif isinstance(nested, (list, tuple,)):
        for index, value in enumerate(nested):
            if isinstance(value, dict):
                for key1, value1 in value.items():
                    ok = match_key(ignore_list, key1)
                    if ok:
                        subkey = str(index) + "." + key1
                        new_key = create_key(top, prefix, subkey)
                        assign(new_key, value1, True)
                    else:
                        new_key = create_key(top, prefix, str(index))
                        assign(new_key, value, False)

            else:
                new_key = create_key(top, prefix, str(index))
                assign(new_key, value, False)

    else:
        return ("Not a Valid input")


def create_key(top, prefix, subkey):
    key = prefix
    if top:
        key += subkey
    else:
        key += "." + subkey

    return key


def match_key(ignorelist, value):
    for element in ignorelist:
        if element == value:
            return True

    return False

"""
def insert_data(msg, ignorelist):
    msg = json.loads(msg)

    field = flattening(msg, "", ignorelist)
    print(field)

    client = InfluxDBClient(database="python_influxdemo")
    client.create_database("python_influxdb_demo")

    points = [{
        "measurement": 'demo',
        "tags": {},
        "fields": field
    }]
    client.write_points(points)
"""

data = {"intdata": [10, 24, 43, 56, 45, 78],
        "floatdata": [56.67, 45.68, 78.12],
        "nested_data": {
            "key1": "string_data with spaces",
            "key2": [45, 56],
            "key3": [60.8, 45.78]
        }}
data = json.dumps(data)
ignore = ["floatdata"]
# insert_data(data, ignore)
