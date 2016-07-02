from rest_framework import serializers
from post.models import User
from post.models import Post
from post.models import PostAttributes
from userprofile.serializers import UserSerializer


class PostAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostAttributes
        fields = ( 'id','name','value')


class PostSerializer(serializers.ModelSerializer):
    #user = UserSerializer(many=False, read_only=True)  # This will print all user details
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Post
        fields = ('user','id','title','description','title','rentperday','facilities','avail_start_date','avail_end_date','status','is_active','is_verified','keywords','address','street','city','pincode','state','country')
        read_only_fields = ('id','is_active','is_verified')         
        #exclude=('user',)

'''
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        #fields = ( 'emailid','phone_number','first_name','last_name','posts')
        #read_only_fields = ('id',)
'''
