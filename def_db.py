import datetime
import pymongo
import os
import glob
import shlex
import subprocess
from subprocess import call
# stdout=subprocess.PIPE, stderr=subprocess.PIPE,
# path = '/home/cyber/Desktop/files/*'
path = '//10.100.0.60/computers/username/*.*'


def check_path():
    try:
        share_auth = 'net use \\\\10.100.0.60 /USER:qwe\\qwe.qwe qwe'
        test = subprocess.run(
            share_auth, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        # test.returncode == 0 working
        # test.returncode == 2 not working ,already connected or something else
        if test.returncode == 2:
            print(test.stderr)
        if test.returncode == 0:
            print(test.stdout)
    except subprocess.TimeoutExpired:
        print('Error')


def conn_db():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myclient.test
    print(db)
    upload_db = myclient.my_db
    create_data = upload_db.user_data
    return create_data


def close_conn():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    myclient.close()


def create_db():
    create_data = conn_db()
    users = new_users_list()
    insert_data = create_data.insert_many(users)
    return create_db


def create_users_list():
    users = []
    for filename in glob.glob(os.path.join(path)):
        with open(filename, "r") as file:
            for line in file:
                s = line.split()
                if len(s) != 3:
                    users.append(
                        {'comp_name': s[0].lower(), 'u_name': s[1].lower(), 's_name': None, 'ip': None})
                else:
                    users.append({'comp_name': s[0].lower(
                    ), 'u_name': s[1].lower(), 's_name': None, 'ip': s[2][:-1]})
    return users


def new_users_list():
    new_users = create_users_list()
    for s in new_users:
        if '.' in s['u_name']:
            a = s['u_name'].split('.')
            s.update(u_name=a[0], s_name=a[1])
        else:
            s.update(s_name=None)
    return new_users


def drop_user_data():
    create_data = conn_db()
    create_data.drop()


def check():
    create_data = conn_db()
    db_id = create_data.find_one()
    if db_id == None:
        print('creating db...')
        create_db()
    gen_time = create_data.find_one()['_id'].generation_time
    return gen_time


def user_search():
    try:
        user_data = conn_db()
        while True:
            user_input = input(
                'Enter username for search ( Type "c" for compname''): ').lower().split(' ')
            first = user_input[0]
            if 'close' in user_input:
                print('\nProgram closed...')
                break
            if first == 'c':
                comp = input('Enter compname for search:').strip().lower()
                query = {'comp_name': {'$regex': "^"+comp}}
            elif len(user_input) == 1:
                query = {'u_name': {'$regex': "^"+user_input[0]}}
            else:
                query = {'u_name': {'$regex': "^" +
                                    user_input[0]}, 's_name': {'$regex': "^"+user_input[1]}}
            query_handle(query)
    except KeyboardInterrupt:
        print('\nProgram closed...')


def query_handle(query):
    user_data = conn_db()
    for y in user_data.find(query):
        name = y.get('u_name')
        sname = y.get('s_name')
        if sname == None:
            sname = ' '
        comp = y.get('comp_name')
        ip = y.get('ip')
        print('*'*55)
        print((name+'.'+sname).ljust(20), comp.center(20), ip)
    print('='*55)


def test():
    # check_path()
    day = str(datetime.date.today())
    gen_time = check()
    if day not in str(gen_time):
        print('dropping')
        drop_user_data()
        create_db()
    user_search()
    close_conn()


test()
