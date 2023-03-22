import json
import os
import pymongo
from prettytable import PrettyTable

# file_patch = 'qwe.json'
# print(file_patch.split('_'))


def connect_db():
    try:
        return pymongo.MongoClient(
            "mongodb://localhost:27017/", serverSelectionTimeoutMS=1
        )
    except pymongo.errors.ServerSelectionTimeoutError as err:
        print(err)


def fill_data():
    myclient = connect_db()
    mydb = myclient["mydatabase"]
    mycol = mydb["data_json"]
    json_file = "qwe.json"
    mycol.drop()
    with open(json_file, 'r') as f:
        data = json.load(f)
# and '.internal' in host['name']
        a = [
            {
                '_id': index,
                'host': host['name'],
                'managed': host['managed']
            }
            for index, host in enumerate(data, start=0)
            if host['name'] != None
        ]
        mycol.insert_many(a)
    return mycol
# host['managed'] == True and


def query():
    mycol = fill_data()
    x = PrettyTable()

    try:
        while True:
            x.field_names = ["name", "hostname", "managed"]
            user_input = input(
                'Enter hostname for search: ').lower()
            if "?" in user_input:
                user_input = user_input.strip("?")
            elif "*" in user_input:
                user_input = user_input.strip("*")

            if user_input == "":
                os.system('clear')
            else:
                myquery = mycol.find(
                    {"host": {"$regex": f"^{user_input}"}}).limit(16)

                if myquery.explain()['executionStats']['nReturned'] != 0:
                    result_list = [[_["_id"], _["host"], _["managed"]]
                                   for _ in myquery]

                    x.add_rows(
                        result_list
                    )
                    x.align['hostname'] = "l"
                    print(x)
                    x.clear()
                else:
                    print(f'{user_input} _-_ not exists')

    except KeyboardInterrupt:
        print('\nClosing...')


query()
