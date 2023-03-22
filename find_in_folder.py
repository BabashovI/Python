import glob, os, pymongo
#=========================
users=[]
path ='//10.100.0.60/computers/username/*.*'
#==========================
def make_list():
	for filename in glob.glob(os.path.join(path)):
		with open(filename, "r") as file:
			for line in file:
				s=line.split()
				if len(s)!=3:
					users.append({'comp_name':s[0],'username':s[1]})
				else:
					users.append({'comp_name':s[0],'username':s[1],'ip':s[2]})

def db_create():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["mydatabase"]


print(users)





		