from users.models import User,Post
from users.serializers import UserSerializer,PostSerializer

from rest_framework import permissions
from rest_framework.decorators import permission_classes

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics


@permission_classes((permissions.AllowAny,))
class UserList(APIView):
    def get(self,request,format=None):
        users = User.objects.all();
        serializer = UserSerializer(users,many=True)
        print serializer.data
        return Response(serializer.data)

    def post(self,request,format=None):    
        print request.data
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


@permission_classes((permissions.AllowAny,))
class PostList(APIView):
    def get(self,request,user_pk,format=None):
        posts = Post.objects.all();
        serializer = PostSerializer(posts,many=True)
        #print serializer.data
        return Response(serializer.data)

    def post(self,request,user_pk,format=None):    
        request.data['user']= user_pk
        print request.data
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        print '************************************************************'
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
         print post
         request.data["user"]=user_pk   
         serializer = PostSerializer(post,data=request.data)     
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,user_pk,pk,format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
