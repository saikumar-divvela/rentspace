from rest_framework import serializers
'''
from post.models import User
from post.models import Post
from post.models import PostAttributes
from post.models import Comment
from post.models import Image



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

'''
