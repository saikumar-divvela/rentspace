from users.models import User
from users.serializers import UserSerializer

from rest_framework import status,permissions
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response




@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def user_list(request,format=None):
    if request.method == 'GET':
        users = User.objects.all();
        serializer = UserSerializer(users,many=True)
        print serializer.data
        return Response(serializer.data)

    elif request.method == 'POST':
        print request.data
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def user_detail(request, pk,format=None):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
         serializer = UserSerializer(user,data=request.data)     
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)   
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
