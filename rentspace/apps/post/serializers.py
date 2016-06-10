from rest_framework import serializers
from post.models import User
from post.models import Post
from post.models import PostAttributes


class PostAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttributes
        fields = ( 'id','name','value')


class PostSerializer(serializers.ModelSerializer):
    attributes = PostAttributeSerializer(read_only=True,many=True)
    class Meta:
        model = Post
        fields = ('id','description','rentperday','facilities','avail_start_date','avail_end_date','status','is_active','is_verified','keywords')
        #read_only_fields = ('id',)         
        #exclude=('user',)


'''
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        #fields = ( 'emailid','phone_number','first_name','last_name','posts')
        #read_only_fields = ('id',)
'''