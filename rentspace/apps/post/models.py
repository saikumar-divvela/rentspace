from django.db import models

from homepage.models import *
from userprofile.models import User



class  Post(Address,object):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    title = models.CharField(max_length=100)
    description  = models.CharField(max_length=40)
    rentperday  = models.IntegerField(default=0,blank=True)
    facilities = models.CharField(max_length=512,blank=True)
    avail_start_date = models.DateField(null=True)
    avail_end_date = models.DateField(null=True)
    status  =  models.CharField(max_length=10,choices=STATE,default=PENDING)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    keywords = models.CharField(max_length=50,blank=True)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    

    def __str__(self):
        return self.description

    def __setitem__(self, key, value):
        object.__setattr__(self, key, value)

    class Meta:
        ordering = ('id',)
        db_table = "post"

class PostAttributes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='attributes')
    name = models.CharField(max_length=40,blank=True)
    value = models.CharField(max_length=40,blank=True)
    class Meta:
        ordering = ('id',)
        db_table = "post_attribute"


class  PostPhoto(models.Model):
    photo = models.ImageField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='postphotos')
    class Meta:
        ordering = ('id',)
        db_table = "images"

'''
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    reviewedby = models.ForeignKey(User, null=True, on_delete=models.CASCADE,related_name='comments')
    username  = models.CharField(max_length=50,blank=True)
    description = models.CharField(max_length=100,blank=True)
    status = models.CharField(max_length=10,blank=True,choices=STATE,default=PENDING)

    class Meta:
        ordering = ('id',)
        db_table = "comment"
'''
