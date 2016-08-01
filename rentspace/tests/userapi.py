import requests
from random import randint
import json
import cgi  

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


def update_profile_data(profile,num):
    data ={}
    data["username"] = profile["username"]
    data["first_name"] = profile["first_name"]+"_updated"
    data["last_name"] =  profile["last_name"]+"_updated"
    data["phone_number"] = profile["phone_number"]
    data["address"] ="address_"+num
    data["street"] ="street_"+num
    data["city"]   ="city_"+num
    data["pincode"] = "523155"
    data["state"] = "state_"+num
    data["country"] ="country_"+num
    return data



def register_user(url,data,headers):
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


def get_user_profile(url,data,headers):
    print ("Get User profile")
    resp = requests.get(url,data=data,headers= headers)

    print ("Request:")
    show(resp.url,data,headers)


    print ("Response:")
    show(resp.status_code,resp.headers,resp.encoding)
    print (resp.json())


def update_user_profile(url,data,headers):
    print ("Update User profile")
    resp = requests.put(url,data=data,headers= headers)

    print ("Request:")
    show(resp.url,data,headers)


    print ("Response:")
    show(resp.status_code,resp.headers,resp.encoding)
    print (resp.json())


def uploadfile(url,files,headers):
    print ("You hit file upload")
    resp = requests.put(url,files=files,headers= headers)

    print ("Request:")
    show(resp.url,files,headers)


    print ("Response:")
    show(resp.status_code,resp.headers,resp.encoding)
    print (resp.json())


def downloadfile(url,headers):
    print ("You hit file download")
    resp = requests.get(url,headers= headers)
    show(resp.status_code,resp.headers,resp.encoding)
    #print (resp.content)
    value,params = cgi.parse_header(resp.headers["content-disposition"])
    print (params["filename"])
    with open(params["filename"], 'wb') as output:
        output.write(resp.content)




def main():
    ### URLS ####
    #host_address="http://localhost:8000"
    host_address="http://saikumar.pythonanywhere.com"
    reguser_url=host_address+"/api/register"
    login_url=host_address+"/api/login"
    logout_url = host_address+"/api/logout"
    user_profile_url= host_address+"/api/profile"

    headers={}
    headers["Content-Type"] = "application/json"
    headers["Accept"]="application/json"

    num = randint(100, 999) 

    ## REG USER
    reg_data = reguser_data(str(num))
    json_data = json.dumps(reg_data)
    register_user(reguser_url,json_data,headers)


    ## LOGIN USER
    login_data = {}
    login_data["username"] =  reg_data["username"]
    login_data["password"] =  reg_data["password"]
    json_data = json.dumps(login_data)

    token = login_user(login_url,json_data,headers)
    headers["Authorization"]="Token "+token

    ## GET USER PROFILE
    get_user_profile(user_profile_url,data={},headers=headers)

    ## Update USER PROFILE
    profile_data = update_profile_data(reg_data,str(num))
    json_data = json.dumps(profile_data)
    update_user_profile(user_profile_url,data=json_data,headers=headers)

    ## GET USER PROFILE
    get_user_profile(user_profile_url,data={},headers=headers)

    ## LOGOUT USER
    logout_user(logout_url,data={},headers=headers)


def main1():
    host_address="http://localhost:8000"
    file_upload_url=host_address+"/api/photoid"
    files = {'file': open('test.py','rb')}
    token = "ca9367427dc32fc6011f26021e6284045e021c8d"    

    headers={}
    #headers["Content-Type"] = "multipart/form-data"  # Don't enable this otherwise will fail
    headers["Accept"]="application/json"
    headers["Authorization"]="Token "+token

    # upload file
    uploadfile(file_upload_url,files=files,headers=headers)

    # download file
    downloadfile(file_upload_url,headers=headers)


    


if __name__ == "__main__":
   main()
