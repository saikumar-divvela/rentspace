from users.models import User,Post,PostAttributes,Image
from users.serializers import UserSerializer,PostSerializer,PostAttributeSerializer,ImageSerializer,CommentSerializer

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser, FormParser

from rest_framework import permissions
from rest_framework.decorators import permission_classes

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from wsgiref.util import FileWrapper


import json
import os
import uuid

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@permission_classes((permissions.AllowAny,))
class UserList(APIView):
    def get(self,request,format=None):
        users = User.objects.all();
        serializer = UserSerializer(users,many=True)
        print (serializer.data)
        return Response(serializer.data)

    def post(self,request,format=None):    
        print (request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
class UserDetail(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
         user = self.get_object(pk)
         serializer = UserSerializer(user,data=request.data)     
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_status(self,request,pk,format=None):
        user = self.get_object(pk)
        
        output = {}
        output["is_email_verified"] = user.is_email_verified
        output["is_phone_verified"] = user.is_phone_verified
        output["is_id_verified"] = user.is_id_verified
        return Response(output)

@csrf_exempt
def user_status(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404
    
    if request.method == "GET":
        output = {}
        output["is_email_verified"] = user.is_email_verified
        output["is_phone_verified"] = user.is_phone_verified
        output["is_id_verified"] = user.is_id_verified
                
        serializer = UserSerializer(user)
        return JSONResponse(output)


    elif request.method == "PUT":
         data = JSONParser().parse(request)
         for key,value in data.items():
            user[key]=value    
         user.save()

         serializer = UserSerializer(user)
         return JSONResponse(serializer.data)  
         #return Response(serializer.data) 



@permission_classes((permissions.AllowAny,))
class PostList(APIView):
    def get(self,request,user_pk,format=None):
        user =UserDetail().get_object(user_pk)
        posts = Post.objects.filter(user__id=user_pk);
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self,request,user_pk,format=None):    
        user =UserDetail().get_object(user_pk)
        request.data["user"]= user_pk
        print (request.data["attributes"])
        serializer = PostSerializer(data=request.data)
        print (serializer)
        if serializer.is_valid():
            serializer.save()
            add_post_attributes(request.data["attributes"],serializer.data["id"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        print ("************************************************************")
        serializer.save(user=self.request.user)


@permission_classes((permissions.AllowAny,))
class PostDetail(APIView):
    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, user_pk, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request,user_pk, pk, format=None):
         post = self.get_object(pk)
         print (post)
         request.data["user"]=user_pk   
         serializer = PostSerializer(post,data=request.data)     
         if serializer.is_valid():
            serializer.save()
            update_post_attributes(request.data["attributes"],serializer.data["id"])
            return Response(serializer.data)   
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,user_pk,pk,format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def add_post_attributes(attributelist,post_id):
    for attribute in attributelist:
        attr_data = {}
        attr_data["post"]=post_id
        for name,value in attribute.items():    
            attr_data["name"]=name
            attr_data["value"]=value
            attr_serializer = PostAttributeSerializer(data=attr_data)
            if attr_serializer.is_valid():
                attr_serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def update_post_attributes(attributelist,post_id):
    postattributes = PostAttributes.objects.filter(post__id=post_id);
    for attribute in postattributes:
        attribute.delete()
    add_post_attributes(attributelist,post_id)

@csrf_exempt
def post_status(request,user_pk,pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404
    
    if request.method == "GET":
        output = {}
        output["status"] = post.status
        output["is_verified"] = post.is_verified
        output["is_active"] = post.is_active
                
        serializer = PostSerializer(post)
        return JSONResponse(output)


    elif request.method == "PUT":
         data = JSONParser().parse(request)
         for key,value in data.items():
            post[key]=value    
         post.save()

         serializer = PostSerializer(post)
         return JSONResponse(serializer.data)  
         #return Response(serializer.data) 


@permission_classes((permissions.AllowAny,))
class PostAttributeList(APIView):
    def get(self,request,user_pk,post_pk,format=None):
        postattributes = PostAttributes.objects.filter(post__id=post_pk)
        serializer = PostAttributeSerializer(postattributes,many=True)
        return Response(serializer.data)

    def post(self,request,user_pk,post_pk,format=None):    
        print (request.data)
        update_post_attributes(request.data["attributes"],post_pk)
        postattributes = PostAttributes.objects.filter(post__id=post_pk)
        serializer = PostAttributeSerializer(postattributes,many=True)
        return Response(serializer.data)

    def put(self,request,user_pk,post_pk,format=None):    
        print (request.data)
        update_post_attributes(request.data["attributes"],post_pk)
        postattributes = PostAttributes.objects.filter(post__id=post_pk)
        serializer = PostAttributeSerializer(postattributes,many=True)
        return Response(serializer.data)


# Get -> returns all photos of given post
# Post -> Adds one photo to post    
# example curl -X POST -H "Content-Type: application/json"  -d '{"title": "test pic12","description": "this is a test pic12", "filetype": "test type"}' -F "filedata=@a.txt" http://localhost:8000/users/1/posts/2/images/
# Delete -> Delete all photos of the post
@permission_classes((permissions.AllowAny,))
class ImageList(APIView):
    #parser_classes = (FileUploadParser, )    
    parser_classes = (MultiPartParser, FormParser,)

    def get(self,request,user_pk,post_pk,format=None):
        print ("Get request for all images")
        post =PostDetail().get_object(post_pk)
        images = Image.objects.filter(post__id=post_pk) 
        serializer = ImageSerializer(images,many=True)
        return Response(serializer.data)

    def post(self,request,user_pk,post_pk,format=None):    
        print ("Post request for all images")
        print (request.data)
        tmpdir = "/tmp/media"
        uploaded_file = request.FILES['filedata']
        filename =   str(uploaded_file)      
    
        if not os.path.exists(os.path.join(tmpdir,"user-"+user_pk,"post-"+post_pk)):
            os.makedirs(os.path.join(tmpdir,"user-"+user_pk,"post-"+post_pk))

        destfile = os.path.join(tmpdir,"user-"+user_pk,"post-"+post_pk,filename)

        with open(destfile, 'wb+') as temp_file:
            for chunk in uploaded_file.chunks():
                temp_file.write(chunk)

        request.data["filename"] =  filename
        request.data["filepath"] =  destfile
        request.data["url"] = uuid.uuid4()
        request.data["post"]= post_pk
        request.data["size"] = os.path.getsize (destfile)

        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,user_pk,post_pk,format=None):    
        post =PostDetail().get_object(post_pk)
        images = Image.objects.filter(post__id=post_pk) 
        for image in images:
            image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

# Get -> returns details of one image
# Delete -> Delete the selected image
@permission_classes((permissions.AllowAny,))
class ImageDetail(APIView):
    def get_object(self,pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise Http404

    def get(self, request, user_pk,post_pk,pk, format=None):
        print ("Get request for one images")
        image = self.get_object(pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)
    
    def delete(self,request,user_pk,post_pk,pk,format=None):
        print ("Deleting selected images")
        image = self.get_object(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes((permissions.AllowAny,))
class ImageDownload(APIView):
    def get(self,request,pk,format=None):
        print (pk)
        image =  Image.objects.filter(url=pk)[0]
        fileformat='raw'
        if fileformat == 'raw':
            out_file = open(image.filepath, 'rb')
            response = HttpResponse(FileWrapper(out_file), content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename="%s"' % image.filename
            return response

'''
@permission_classes((permissions.AllowAny,))
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@permission_classes((permissions.AllowAny,))
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''
