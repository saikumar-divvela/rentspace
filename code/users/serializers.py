from rest_framework import serializers
from users.models import User
from users.models import Post



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #fields = ('id','description','user')
        read_only_fields = ('user',)

class UserSerializer(serializers.ModelSerializer):
    #posts = PostSerializer(many=True)
    class Meta:
        model = User
        #fields = ( 'emailid','phone_number','first_name','last_name','posts')
        read_only_fields = ('id',)

