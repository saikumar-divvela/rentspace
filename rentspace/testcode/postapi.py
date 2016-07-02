import requests
from userapi import *
from random import randint
import json

def addpost_data(num):
    data = {}
    data["title"] = "property_"+num
    data["description"] = "property_"+num
    data["rentperday"] = int(num)
    data["facilities"] =  "internet,ac,hotwater"
    data["address"] ="address_"+num
    data["street"] ="street_"+num
    data["city"]   ="city_"+num
    data["pincode"] = "523155"
    data["state"] = "state_"+num
    data["country"] ="country_"+num
    return data


def addpost(url,data,headers):
    print ("Adding post")
    resp = requests.post(url,data=data,headers= headers)

    print ("Request:")
    show(resp.url,data,headers)


    print ("Response:")
    show(resp.status_code,resp.headers,resp.encoding)
    print (resp.json())
    return resp.json()["data"]["id"]


def getposts(url,data,headers):
    print ("Get all posts")
    resp = requests.get(url,data=data,headers= headers)

    print ("Request:")
    show(resp.url,data,headers)

    print ("Response:")
    show(resp.status_code,resp.headers,resp.encoding)
    print (resp.json())


def getpost(url,data,headers):
    print ("Get post details")
    resp = requests.get(url,data=data,headers= headers)

    print ("Request:")
    show(resp.url,data,headers)

    print ("Response:")
    show(resp.status_code,resp.headers,resp.encoding)
    print (resp.json())


def updatepost(url,data,headers):
    print ("Update post details")
    resp = requests.put(url,data=data,headers= headers)

    print ("Request:")
    show(resp.url,data,headers)

    print ("Response:")
    show(resp.status_code,resp.headers,resp.encoding)
    print (resp.json())


def deletepost(url,data,headers):
    print ("Delete post")
    resp = requests.delete(url,data=data,headers= headers)

    print ("Request:")
    show(resp.url,data,headers)

    print ("Response:")
    show(resp.status_code,resp.headers,resp.encoding)
    print (resp.text)

def update_post_data(postdata, num):
    data = {}
    data["title"] = postdata["title"]+"_updated"
    data["description"] = postdata["description"]+"_updated"
    data["rentperday"] = postdata["rentperday"]
    data["facilities"] =  "internet,ac,hotwater"
    data["address"] = postdata["address"]+"_updated"
    data["street"] = postdata["street"]+"_updated"
    data["city"]   =postdata["city"]
    data["pincode"] = postdata["pincode"]
    data["state"] =  postdata["state"]
    data["country"] =postdata["country"]
    return data

def main():
    ## URLS
    num = randint(1000, 1400) 

    host_address="http://localhost:8000"
    login_url=host_address+"/api/login"
    logout_url = host_address+"/api/logout"

    get_add_post_url=host_address+"/api/posts"
    post_url= host_address+"/api/posts/"


    headers = {}
    headers["Content-Type"] = "application/json"
    headers["Accept"]="application/json"


    ## LOGIN USER
    login_data = {}
    login_data["username"] =  "test288@test288.com"
    login_data["password"] =  "test288"
    json_data = json.dumps(login_data)   
    token = login_user(login_url,json_data,headers=headers)
    headers["Authorization"]="Token "+token


    ## ADD POST
    post_data = addpost_data(str(num))
    json_data = json.dumps(post_data)   
    post_id = addpost(get_add_post_url,data=json_data,headers=headers)

    ## GET ALL POST
    getposts(get_add_post_url,data={},headers=headers)

    post_url = post_url+ str(post_id)
    print (post_url)

    ## GET A POST DETAILS
    getpost(post_url,data={},headers=headers)


    ## UPDATE POST DETAILS
    updatepost_data = update_post_data(post_data,str(num))
    json_data = json.dumps(updatepost_data)
    updatepost(post_url,data=json_data,headers=headers)

    ## GET A POST DETAILS
    getpost(post_url,data={},headers=headers)


    ## DELETE POST
    #deletepost(post_url,data={},headers=headers)

    ## GET A POST DETAILS
    getpost(post_url,data={},headers=headers)

    
    ## LOGOUT USER
    logout_user(logout_url,data={},headers=headers)


if __name__ == "__main__":
   main()
