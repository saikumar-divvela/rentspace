from rest_framework import serializers
from userprofile.models import User
#from post.serializers import PostSerializer


class UserRegSerializer(serializers.ModelSerializer):
	class Meta:
		model  = User
		fields = ('email','password')



class UserSerializer(serializers.ModelSerializer):
    #posts = PostSerializer(read_only=True,many=True)
    
    class Meta:
        model = User
        fields = ( 'id','email','first_name','last_name','phone_number','date_of_birth','gender','is_staff','address','street','city','pincode','state','country')
        read_only_fields = ('id','email','is_staff')
        #exclude=('id',)



