#/usr/bin/python


class User():
    def __init__(self):
        pass
    is_id_verified=""
    is_email_verified =""
    is_phone_verified=""
    key ="test"
    '''
    def __setitem__(self, key, value):
        print key,value
        object.__setattr__(self, key, value)
    '''    
    '''
    def __setattr__(self, name, value):
        print name,value
    '''

u =User()
d = {"is_id_verified": "T", "is_email_verified": "F", "is_phone_verified": "F","X":"Y"}
for key,value in d.items():
    #u[key] = value
    print key

u.isss_id_verified="F"

u1 = User()
u2 = User()
u3 = User()

u1.key="test1"
print u1.key
print User.key
u3.xyz1="test3"
print u3.xyz1
