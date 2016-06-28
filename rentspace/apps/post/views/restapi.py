from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser, FormParser
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.http import HttpResponse

from userprofile.models import User
from post.models import Post
from post.serializers import PostSerializer


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
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
         post = self.get_object(pk)
         print (post)
         request.data["user"]=request.user.id
         serializer = PostSerializer(post,data=request.data)     
         if serializer.is_valid():
            serializer.save()
            #update_post_attributes(request.data["attributes"],serializer.data["id"])
            return Response(serializer.data)   
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        post = self.get_object(pk)
        post.is_active = False
        post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Handles add post, get posts
@permission_classes((IsAuthenticated,))
class Posts(APIView):
    def get(self,request,format=None):
        print('You hit Posts get request')
        posts = Post.objects.filter(user__id=request.user.id,is_active=True);
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):    
        print ('You hit add post')
        data = JSONParser().parse(request)
        
        data["user"] = request.user.id
        print(data)
        serializer = PostSerializer(data=data)
        print (serializer)
        if serializer.is_valid():
            print ('just before saving')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@csrf_exempt
@api_view(['GET','PUT'])
@permission_classes((IsAuthenticated,))
def post_status(request,pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404
    
    if request.method == "GET":
        output = {}
        output["status"] = post.status
        output["is_verified"] = post.is_verified
               
        serializer = PostSerializer(post)
        return JSONResponse(output)

    elif request.method == "PUT":
         data = JSONParser().parse(request)
         
         post["is_verified"] = data["is_verified"]
         post["status"] = data["status"]
         post.save()

         serializer = PostSerializer(post)
         return JSONResponse(serializer.data) 
         
