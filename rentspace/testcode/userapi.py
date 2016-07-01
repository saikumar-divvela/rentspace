import requests
from random import randint

def show(*args):
    print (args)

def reguser_data(num):
    data = {}
    data["username"] = "test"+num+"@test"+num+".com"
    data["password"] = "test"+num
    data["first_name"] = "test"+num+"_fn"
    data["last_name"] = "test"+num+"_ln"
    data["phone_number"] = num
    return data


def register_user(url,data,header):
    print ("Register User:")

    resp = requests.post(url,data=data,headers= headers)
    
    print ("Request:")
    show(resp.url,data,headers)


    print ("Response:")
    show(resp.status_code,resp.headers,resp.encoding)
    print (resp.json())


    

def login_user(url,data,headers):
    print ("Login user")
    resp = requests.post(url,data=data,headers= headers)

    print ("Request:")
    show(resp.url,data,headers)


    print ("Response:")
    show(resp.status_code,resp.headers,resp.encoding)
    print (resp.json())

    return resp.json()["token"]


def logout_user(url,data,headers):
    print ("Logout user")
    resp = requests.post(url,data=data,headers= headers)

    print ("Request:")
    show(resp.url,data,headers)


    print ("Response:")
    show(resp.status_code,resp.headers,resp.encoding)
    print (resp.json())


### URLS ####
host_address="http://localhost:8000"
reguser_url=host_address+"/api/register"
login_url=host_address+"/api/login"
logout_url = host_address+"/api/logout"

headers = {}
headers["Accept"]="application/json"

num = randint(100, 999) 

## REG USER
reg_data = reguser_data(str(num))
register_user(reguser_url,reg_data,headers)


## LOGIN USER

login_data = {}
login_data["username"] =  reg_data["username"]
login_data["password"] =  reg_data["password"]
token = login_user(login_url,login_data,headers)


## LOGOUT USER
headers["Authorization"]="Token "+token
logout_user(logout_url,data={},headers=headers)

