import datetime, pymongo, os, glob, time

path = '//10.100.0.60/computers/username/*.*'
#path = 'C:/Users/Main/Google Drive/Desktop/Python/files/*.*'
def conn_db():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	upload_db = myclient.my_db
	create_data = upload_db.user_data
	myclient.close()
	return create_data

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
				s=line.split()
				if len(s) != 3:
					users.append({'comp_name':s[0].lower(), 'u_name':s[1].lower(), 's_name':None, 'ip':None})
				else :
					users.append({'comp_name':s[0].lower(), 'u_name':s[1].lower(), 's_name':None, 'ip':s[2]})
	return users

def new_users_list():
	new_users = create_users_list()
	for s in new_users:
		if '.' in s['u_name']:
			a=s['u_name'].split('.')
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
		create_db()
		gen_time = db_id['_id'].generation_time
	else:
		gen_time = db_id['_id'].generation_time
	return gen_time

def user_search():
	try:
		user_data = conn_db()
		while True:
			user_input = input('Enter username for search: ').lower().split(' ')
			if 'close' in user_input:
				print('Program closed...')
				break
			else:
				user_find = {'u_name':{'$regex':user_input[0]},'s_name':{'$regex':user_input[1]}}
				for y in user_data.find(user_find):
					name = y.get('u_name')
					sname = y.get('s_name')
					comp = y.get('comp_name')
					ip = y.get('ip')
					print('_'*55)
					print((name+'.'+sname).ljust(20),comp.center(20),ip)
				print('_'*55)
	except KeyboardInterrupt as k:
		print('Program closed...')

def test():
	day = str(datetime.date.today())
	gen_time = check()
	if day not in str(gen_time):
		drop_user_data()
		create_db()
	user_search()
test()