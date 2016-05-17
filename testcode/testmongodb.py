#!/usr/bin/python

from mongoengine import *
import json

db ="rentspace"
host="mongodb://localhost:27017"
# host='mongodb://admin:qwerty@localhost/production'  ## connects to production database using admin user and qwerty password
username=""
password=""
connect(db, username=username, password=password,host=host)


## This schema is never passed to Mongodb. Only schema checks happen at application level
class User(Document):
    email = StringField(required=True)
    password = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    phone_number = StringField(max_length=10)

'''
from pymongo import MongoClient

client = MongoClient()
db = client["rentspace"]
print client

def adduser(user):
    print db.users.insert_one(user)
    print "Adding user"

def updateuser(user):
    print "updating user"
    results = db.users.update_one({"emailid":user["emailid"]},{"$set":user},upsert=False)
    print results.matched_count
    print results.modified_count

def deleteuser(username):
    print "Deleting user %s"%(username)
    user ={}
    user["emailid"] = username
    result = db.users.delete_one(user)
    print result.deleted_count

def getuser(username):
    print "Get user details"
    user["emailid"] = username
    cursor = db.users.find(user)
    print cursor
    for document in cursor:
        print document

def getallusers():
    print "All users"
    cursor = db.users.find()
    for rec in cursor:
        print rec

def deleteallusers():
    print "Deleting all users..."
    result = db.users.delete_many({})
    print result.deleted_count


user ={}
user["firstname"] ="saikumar"
user["lastname"] ="divvela"
user["emailid"] ="saikumar.divvela@gmail.com"
user["password"]="test"
user["mobilenumber"] = "9845198763"



#deleteuser("saikumar.divvela@gmail.com")

deleteallusers()
adduser(user)
getuser(user["emailid"])
getallusers()
user["mobilenumber"] = "12345"
updateuser(user)
getallusers()
'''

def adduser(user):
    u = User(email=user["email"],password=user["password"], first_name=user["first_name"],last_name=user["last_name"],phone_number=user["phone_number"]).save()
    print u.to_json()
    return True if u.to_json else False


def deleteuser(email):
    count = User.objects(email=email).delete()
    
    return True if count > 0 else False


def getuser(email):
    u  = User.objects(email=email)
    print  u.to_json()
    return u.to_json() if u else []


def updateuser(user):
    u  = User.objects(email=user["email"])
    d = json.loads(u.to_json())
    print d
    u[0].first_name ='test1111'
    u[0].save()
    #u.update_one({'first_name':'test_name'})
    #u.update_one(user)
    '''
    print len(d)
    nu = User()
    for key in d[0]:
        nu[key] = d[0][key] 

    for key in user:
        nu[key] = user[key]

    print nu
    '''

def getallusers():
    u = User.objects.all()
    print u.to_json()
    return u.to_json()


user ={}
user["first_name"] ="saikumar"
user["last_name"] ="divvela"
user["email"] ="saikumar.divvela@gmail.com"
user["password"]="test"
user["phone_number"] = "9845198763"    



print deleteuser('12333')
print deleteuser('saikumar.divvela@gmail.com')
adduser(user)
getuser('saikumar.divvela@gmail.com')
getallusers()
updateuser(user)
getuser('saikumar.divvela@gmail.com')
print deleteuser('saikumar.divvela@gmail.com')
getallusers()


'''
jsondata =  User.objects.all().to_json()
print jsondata
print u
#print u['first_name']
#print User.objects.get({"emailid":"ross@example.com"})
'''
