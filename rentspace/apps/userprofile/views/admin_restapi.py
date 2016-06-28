
from django.http import HttpResponse
from django.http import Http404
from rest_framework import status
from userprofile.models import User
from userprofile.serializers import UserSerializer

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
        print (request.session)
        print (request.session.keys())
        print (request.session.items())
        #print (serializer.data)
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