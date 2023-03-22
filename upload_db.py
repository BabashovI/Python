import glob, os, pymongo, datetime
#============================================#
day = datetime.date.today().day
users = []
path = '//10.100.0.60/computers/username/*.*'
for filename in glob.glob(os.path.join(path)):
		with open(filename, "r") as file:
			for line in file:
				s=line.split()
				if len(s) != 3:
					users.append({'comp_name':s[0].lower(),'username':s[1].lower(),'date':day})
				else:
					users.append({'comp_name':s[0].lower(),'username':s[1].lower(),'ip':s[2],'date':day})
#print(users)

print('========================================\n')
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
upload_db = myclient['my_db']
user_data = upload_db["user_data"]
user_data.drop()
print(upload_db.list_collection_names())

insert_users = user_data.insert_many(users)
print('For closing terminal type ''Close'' or just press Ctrl+c\n')

while True:
	user_input = input('Enter username for search: ').strip().lower()
	i = {'username':{'$regex':user_input}}
	if user_input == 'close':
		print('\n'*50)
		break
	else:
		print('=================')
		for y in user_data.find(i):
			name = y.get('username')
			comp = y.get('comp_name')
			ip = y.get('ip')
			#print(len(comp)*5*'=')
			print(name.ljust(20),comp.center(20),ip)
		print('===================================')
	
	

