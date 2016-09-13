from rest_framework.renderers import JSONRenderer

from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


from rest_framework.views import APIView
from rest_framework import status

from django.http import Http404
from django.http import HttpResponse

from userprofile.models import User
from post.models import Post
from post.serializers import PostSerializer

import traceback
import userprofile.error_codes as message


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# handles get post, update post, delete post
@permission_classes((IsAuthenticated,))
class PostDetail(APIView):
    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print ("You hit Get POST REQUEST")
        response = {}
        response["status"] = message.SUCCESS

        try:
            post = self.get_object(pk)
            serializer = PostSerializer(post)
            response["data"]= serializer.data
            print (response)

        except Exception as exp:
            print (exp)
            traceback.print_exc()
            response["status"]= message.ERROR
            response["message"]=str(exp)


        if response["status"] == message.SUCCESS:
            return JSONResponse(response,status=status.HTTP_200_OK)
        else:
            return JSONResponse(response,status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, format=None):
        response = {}
        response["status"] = message.SUCCESS

        try:
            post = self.get_object(pk)
            request.data["user"]=request.user.id
            serializer = PostSerializer(post,data=request.data)
            if serializer.is_valid():
                serializer.save()
                response["data"] = serializer.data
                response["message"] = message.UPDATE_POST_SUCCESS

                #update_post_attributes(request.data["attributes"],serializer.data["id"])
            else:
                response["message"] = serializer.errors

        except Exception as exp:
            print (exp)
            traceback.print_exc()
            response["status"]= message.ERROR
            response["message"]=str(exp)

        if response["status"] == message.SUCCESS:
            return JSONResponse(response,status=status.HTTP_200_OK)
        else:
            return JSONResponse(response,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk,format=None):
        print('You hit delete post request')
        response = {}
        response["status"] = message.SUCCESS

        try:
            post = self.get_object(pk)
            post.is_active = False
            post.save()
            response["message"]= message.DELETE_POST_SUCCESS

        except Exception as exp:
            print (exp)
            traceback.print_exc()
            response["status"]= message.ERROR
            response["message"] = str(exp)

        print (response)
        if response["status"] == message.SUCCESS:
            return JSONResponse(response,status=status.HTTP_204_NO_CONTENT)
        else:
            return JSONResponse(response,status=status.HTTP_400_BAD_REQUEST)


#Handles add post, get posts
@permission_classes((IsAuthenticated,))
class Posts(APIView):
    def get(self,request,format=None):
        print('You hit Posts get request')

        response = {}
        response["status"] = message.SUCCESS

        try:
            posts = Post.objects.filter(user__id=request.user.id,is_active=True);
            serializer = PostSerializer(posts,many=True)
            response["data"]= serializer.data

        except Exception as exp:
            print (exp)
            traceback.print_exc()
            response["status"]= message.ERROR
            response["message"]=str(exp)

        if response["status"] == message.SUCCESS:
            return JSONResponse(response,status=status.HTTP_200_OK)
        else:
            return JSONResponse(response,status=status.HTTP_400_BAD_REQUEST)


    def post(self,request,format=None):
        print ('You hit add post')
        response ={}
        response["status"] = message.SUCCESS

        try:

            data = request.data
            data["user"] = request.user.id
            print(data)
            serializer = PostSerializer(data=data)

            if serializer.is_valid():
                serializer.save()

                response["data"] = serializer.data
                response["message"] = message.CREATE_POST_SUCCESS

            else:
                response["message"] = serializer.errors


        except Exception as exp:
            print (exp)
            traceback.print_exc()
            response["status"]= message.ERROR
            response["message"]=str(exp)


        if response["status"] == message.SUCCESS:
            return JSONResponse(response,status=status.HTTP_201_CREATED)
        else:
            return JSONResponse(response,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT'])
@permission_classes((IsAuthenticated,))
def post_status(request,pk):
    response ={}
    response["status"] = message.SUCCESS

    try:
        post = Post.objects.get(pk=pk)
        if request.method == "GET":
            output = {}
            output["status"] = post.status
            output["is_verified"] = post.is_verified
            response["data"] = output

        elif request.method == "PUT":
            data = request.data
            post["is_verified"] = data["is_verified"]
            post["status"] = data["status"]
            post.save()

            serializer = PostSerializer(post)
            response["data"] = serializer.data

    except Exception as exp:
            print (exp)
            traceback.print_exc()
            response["status"]= message.ERROR
            response["message"]=str(exp)


    if response["status"] == message.SUCCESS:
        return JSONResponse(response,status=status.HTTP_200_OK)
    else:
        return JSONResponse(response,status=status.HTTP_400_BAD_REQUEST)


