from rest_framework import serializers
from users.models import User
from users.models import Post
from users.models import PostAttributes


class PostAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttributes
        #fields = ( 'emailid','phone_number','first_name','last_name','posts')
        #read_only_fields = ('id',)


class PostSerializer(serializers.ModelSerializer):
    attributes = PostAttributeSerializer(read_only=True,many=True)
    class Meta:
        model = Post
        #fields = ('id','description','user')
        #read_only_fields = ('id',)         
        #exclude=('user',)

class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(read_only=True,many=True)
    class Meta:
        model = User
        #fields = ( 'emailid','phone_number','first_name','last_name','posts')
        #read_only_fields = ('id',)
        #exclude=('id',)



