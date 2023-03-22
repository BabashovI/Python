import pymongo
import pytest


def test_mongodb():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = client["mydatabase"]
    mycol = mydb["data_json"]
    a = mycol.find_one('_id')
    #assert a
    assert client.server_info()


# @pytest.fixture(scope="module")
# def mongo_client():
#     client = pymongo.MongoClient("mongodb://localhost:27017/")
#     yield client
#     client.drop_database('test_db')
#     client.close()


# def test_mongodb_connection(mongo_client):
#     test_db = mongo_client['test_db']
#     assert test_db.name in mongo_client.list_database_names()
