from django.http import HttpResponse

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate, logout
import traceback

from userprofile.models import User
from userprofile.serializers import UserSerializer
import userprofile.service as service
import userprofile.error_codes as message


'''
def token_request(request):
    if user_requested_token() and token_request_is_warranted():
        new_token = Token.objects.create(user=request.user)

'''


@api_view(['GET','PUT'])
@permission_classes((IsAuthenticated,))
def photoid(request):
    #parser_classes = (MultiPartParser, FormParser,)
    response ={}
    response["status"] = message.SUCCESS
    try:
        if request.method == "PUT":
            print ('you hit file upload')
            print(request.data)
            user = request.user
            user.idphoto = request.FILES['file']
            user.save()
            print (user.idphoto.path, user.idphoto.name, user.idphoto.url)
            response["message"] = "photo uploaded successfully"

        elif request.method == "GET":
            print ('you hit file download')
            user = request.user
            #print (user.idphoto.path,user.idphoto.name,user.idphoto.url)
            filedata = open(user.idphoto.path, 'rb')

            response = HttpResponse(FileWrapper(filedata), content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename="%s"' % (user.idphoto.name)

            return response

    except Exception as exp:
        print (exp)
        traceback.print_exc()
        response["status"]= message.ERROR
        response["message"]=str(exp)

    if response["status"] == message.SUCCESS:
        return Response(data=response, status=status.HTTP_200_OK)
    else:
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def registeruser(request):
    print ("You Hit registeruser")
    response = {}
    response["status"] = message.SUCCESS
    try:
        data = request.data
        print (data)
        username = data["username"]
        password = data["password"]
        first_name = data["first_name"]
        last_name = data["last_name"]
        phone_number = data["phone_number"]

        print (username, password, phone_number, first_name, last_name)
        response = service.createuser(username, password, first_name, last_name, phone_number)

    except Exception as exp:
        print (exp)
        traceback.print_exc()
        response["status"] = message.ERROR
        response["message"] = str(exp)

    if response["status"] == message.SUCCESS:
        return JSONResponse(response,status=status.HTTP_201_CREATED)
    else:
        return JSONResponse(response,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def userlogin(request):
    print ('You hit login(rest api) request')
    response = {}
    response["status"] = message.SUCCESS
    import re
    regex_content_type = re.compile(r'^CONTENT_TYPE$')
    for header in request.META:
        if regex_content_type.match(header):
            print (header)
            print (request.META[header])
    try:
        data = request.data
        username = data["username"]
        password = data["password"]
        #print (username,password)

        user = authenticate(username=username, password=password)
        print (user)

        if user is not None:
            #login(request, user)    # Login not required , otherwise session is created and is useless

            new_token = Token.objects.get_or_create(user=user)
            print (new_token, new_token[0])
            response["token"] = str(new_token[0])
            response["message"] = message.LOGIN_SUCCESS

        else:
            response["status"] = message.ERROR
            response["message"] = message.USER_NOT_EXISTS

    except Exception as exp:
        print (exp)
        traceback.print_exc()
        response["status"] = message.ERROR
        response["message"] = str(exp)

    print (response)

    if response["status"] == message.SUCCESS:
        return JSONResponse(response, status=status.HTTP_200_OK)
    else:
        return JSONResponse(response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def userlogout(request):
    print ('You hit logout(rest api) request')

    response ={}
    response["status"] = message.SUCCESS
    try:
        if "HTTP_AUTHORIZATION" in request.META.keys():
            token = request.META["HTTP_AUTHORIZATION"]
            print (token)
        print (request.user)

        request.user.auth_token.delete()
        logout(request)   # This is not needed as there is no login

        '''
        for sesskey in request.session.keys():
            print (sesskey)
            del request.session[sesskey]
        request.session.flush()
        '''

        print (request.user)
        response["message"] = message.USER_LOGOUT_SUCCESS

    except Exception as exp:
        print (exp)
        traceback.print_exc()
        response["status"] = message.ERROR
        response["message"] = str(exp)

    if response["status"] == message.SUCCESS:
        return JSONResponse(response, status=status.HTTP_200_OK)
    else:
        return JSONResponse(response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
@permission_classes((IsAuthenticated,))
def user_status(request):
    response = {}
    response["status"] = message.SUCCESS
    print ('You hit user status')
    try:
        if request.method == "GET":
            user = request.user
            output = {}
            output["is_email_verified"] = user.is_email_verified
            output["is_phone_verified"] = user.is_phone_verified
            output["is_id_verified"] = user.is_id_verified
            response["data"] = output

        elif request.method == "PUT":
            data = request.data
            print (data)
            user = request.user
            user.is_id_verified = data["is_id_verified"]
            user.is_phone_verified = data["is_phone_verified"]
            user.is_email_verified = data["is_email_verified"]
            user.save()

            response["status"] = message.SUCCESS
            response["message"] = message.UPDATE_USER_SUCCESS


    except Exception as exp:
        print (exp)
        traceback.print_exc()
        response["status"] = message.ERROR
        response["message"] = str(exp)


    if response["status"] == message.SUCCESS:
        return JSONResponse(response, status=status.HTTP_200_OK)
    else:
        return JSONResponse(response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes((IsAuthenticated,))
def user_profile(request):
    response = {}
    response["status"] = message.SUCCESS
    print ('You hit user profile')

    try:
        if request.method == "GET":
            user = request.user
            serializer = UserSerializer(user)
            print (serializer.data)
            response["data"] = serializer.data

        elif request.method == "PUT":
            data = request.data
            print (data)
            serializer = UserSerializer(request.user,data=data)
            if serializer.is_valid():
                serializer.save()
                response["data"] = serializer.data
                response["message"] = message.UPDATE_USER_SUCCESS
            else:
                response["status"]= message.ERROR
                response["message"] = serializer.errors

    except Exception as exp:
        print (exp)
        traceback.print_exc()
        response["status"]= message.ERROR
        response["message"]= str(exp)


    if response["status"] == message.SUCCESS:
        return JSONResponse(response,status=status.HTTP_200_OK)
    else:
        return JSONResponse(response,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def testlogin(request):
    print (request.user.is_authenticated())
    print (request.user)
    print (request.auth)


    output = {}

    output["message"] = "If you see this it means you are logged in"
    return JSONResponse(output)

"""
    An HttpResponse that renders its content into JSON.
"""
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)