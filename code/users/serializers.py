from rest_framework import serializers
from users.models import User
from users.models import Post
from users.models import PostAttributes
from users.models import Comment
from users.models import Image


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


class ImageSerializer(serializers.ModelSerializer):
    filecontent = serializers.SerializerMethodField()
    class Meta:
        model = Image
        #fields = ( 'emailid','phone_number','first_name','last_name','posts')
        #read_only_fields = ('filepath','filetype',)
        #exclude=('filepath','filetype',)

    def get_filecontent(self, obj):
        #return (now() - obj.date_joined).days
        return  obj.filepath


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        #fields = ( 'emailid','phone_number','first_name','last_name','posts')
        #read_only_fields = ('id',)

