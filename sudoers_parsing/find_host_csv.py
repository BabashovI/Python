import os
import pymongo


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
    mycol = mydb["customers"]
    mycol.drop()
    with open('CSV.csv', 'r') as file_obj:
        a = [
            {
                '_id': index,
                'host': host.strip(),
            }
            for index, host in enumerate(file_obj, start=0)
        ]

    mycol.insert_many(a)
    return mycol


def query():
    mycol = fill_data()
    try:
        while True:
            user_input = input(
                'Enter hostname for search: ').lower()
            if "?" in user_input:
                user_input = user_input.strip("?")
            elif "*" in user_input:
                user_input = user_input.strip("*")

            # print(user_input)
            if user_input == "":
                os.system('clear')
            else:
                myquery = mycol.find(
                    {"host": {"$regex": f"^{user_input}"}}).limit(8)
                if myquery.explain()['executionStats']['nReturned'] != 0:
                    for _ in myquery:
                        print(f'{user_input} _-_ {_["host"]}')
                else:
                    print(f'{user_input} _-_ not exists')

    except KeyboardInterrupt:
        print('\nClosing...')


query()
###################################
# with open('hosts1', 'r') as hosts:
#     result = ",".join(line.strip()
#                       for line in hosts.readlines()).split(',')
# cleaned = [i.strip() for i in list(dict.fromkeys(result))]
#     print(i)
#
# myquery = mycol.find({"host": {"$regex": '^salt'}}).limit(3)
# print(myquery.explain()['executionStats']['nReturned'])
# # 'executionStats': {'executionSuccess': True, 'nReturned')
# if myquery.explain()['executionStats']['nReturned'] != 0:
#     for x in myquery:
#         print(f'{x}')
# else:
#     print()
##############################
# mycol = fill_data()
# for _input in cleaned:
#     if "?" in _input:
#         _input = _input.strip("?")
#     elif "*" in _input:
#         _input = _input.strip("*")
#     # print(_input)
#     myquery = mycol.find(
#         {"host": {"$regex": f"^{_input}"}}).limit(1)
#     if myquery.explain()['executionStats']['nReturned'] != 0:
#         for _ in myquery:
#             print(f'{_input} _-_ {_["host"]}\r')
#     else:
#         print(f'{_input} _-_ not exists\r')
