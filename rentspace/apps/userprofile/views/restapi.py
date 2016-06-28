from userprofile.models import User
from userprofile.serializers import UserSerializer

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import userprofile.service as service
from userprofile.error_codes import *

'''
def token_request(request):
    if user_requested_token() and token_request_is_warranted():
        new_token = Token.objects.create(user=request.user)

'''

@api_view(['POST'])
def registeruser(request):
    print  ("You Hit registeruser")
    response ={}

    try:
        data = JSONParser().parse(request)
        if request.method == 'POST':
            username = data["username"]
            password = data["password"]
            first_name = data["first_name"]
            last_name = data["last_name"]
            phone_number =  data["phone_number"]

            print (username,password,phone_number,first_name,last_name)
            response = service.createuser(username,password,first_name,last_name,phone_number) 

    except Exception as exp:            
        response["status"]= ERROR
        response["code"] = ERROR_CODE       
        response["msg"]= ERROR_MSG
    
    return JSONResponse(response)    


@api_view(['POST'])
def userlogin(request):
    print ('You hit login(rest api) request')
    response={}
    response["status"]=ERROR
    #print (request.data)
    try:
        data = JSONParser().parse(request)
        username = data["username"]
        password = data["password"]
        #print (username,password)

        user = authenticate(username=username, password=password)
        print (user)
    
        if user is not None:
            login(request, user)
            new_token = Token.objects.create(user=user)
            print (new_token)
            response["token"] = str(new_token)
            response["status"]= SUCCESS
            response["msg"]= "Login successfull"  
        else:
            response["status"]= ERROR
            response["code"] = ERROR_CODE       
            response["msg"]= "User doesn't exist"  
    
    except Exception as exp:
        print (exp)
        response["status"]= ERROR
        response["code"] = ERROR_CODE       
        response["msg"]= ERROR_MSG                
            
    print (response)       
    return JSONResponse(response)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def userlogout(request):
    print ('You hit logout(rest api) request')

    response={}
    response["status"]= SUCCESS
    response["code"]= SUCCESS_CODE

    try:
        if "HTTP_AUTHORIZATION" in request.META.keys():
            token = request.META["HTTP_AUTHORIZATION"]        
            print (token)

        print (request.user)
        request.user.auth_token.delete()
        logout(request)
        request.session.flush()
        print (request.user)    
        response["msg"]= "User logged out successfully"

    except Exception as exp:
        response["status"]= ERROR
        response["code"] = ERROR_CODE       
        response["msg"]= ERROR_MSG 

    return JSONResponse(response)     


@api_view(['GET','PUT'])
@permission_classes((IsAuthenticated,))
def user_status(request):
    response = {}
    print ('You hit user status')
    try:
        if request.method == "GET":
            user = request.user
    
            response["is_email_verified"] = user.is_email_verified
            response["is_phone_verified"] = user.is_phone_verified
            response["is_id_verified"] = user.is_id_verified
            return JSONResponse(response)

        elif request.method == "PUT":
            data = JSONParser().parse(request)
            print (data)   
            user = request.user
            user.is_id_verified = data["is_id_verified"]
            user.is_phone_verified = data["is_phone_verified"]
            user.is_email_verified = data["is_email_verified"]
            user.save()

            response["status"]= SUCCESS
            response["code"]= SUCCESS_CODE
            response["msg"]= "User status updated successfully"

            return JSONResponse(response)
    except Exception as exp:
        print (exp)
        response["status"]= ERROR
        response["code"] = ERROR_CODE       
        response["msg"]= ERROR_MSG 

    return JSONResponse(response)     


@api_view(['GET','PUT'])
@permission_classes((IsAuthenticated,))
def user_profile(request):
    response = {}
    print ('You hit user profile')
    try:
        if request.method == "GET":
            user = request.user
            serializer = UserSerializer(user)
            return Response(serializer.data)

        elif request.method == "PUT":
            data = JSONParser().parse(request)
            print (data)
            serializer = UserSerializer(request.user,data=data)     
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)   
            print (serializer.errors)
            response["status"]= ERROR
            response["code"] = ERROR_CODE       
            response["msg"]= ERROR_MSG      
            return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as exp:
        print (exp)
        response["status"]= ERROR
        response["code"] = ERROR_CODE       
        response["msg"]= ERROR_MSG 

    return JSONResponse(response)    

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def testlogin(request):
    print (request.user.is_authenticated())
    print (request.user)
    output={}
    #print (request.auth)
    output["msg"] ="If you see this it means you are logged in"
    return JSONResponse(output)    


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        


         