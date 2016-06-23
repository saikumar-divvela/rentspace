from rest_framework import serializers
from userprofile.models import User
#from post.serializers import PostSerializer

class UserSerializer(serializers.ModelSerializer):
    #posts = PostSerializer(read_only=True,many=True)
    class Meta:
        model = User
        fields = ( 'id','email','first_name','last_name','phone_number','date_of_birth','gender','is_active','is_admin','address','street','city','pincode','state','country')
        #read_only_fields = ('id',)
        #exclude=('id',)



