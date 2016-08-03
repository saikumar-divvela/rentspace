from django.db import models

from homepage.models import *
from userprofile.models import User

PG ='PG'
HOUSE='HOUSE'
VILLA='VILLA'
FLAT='FLAT'

HOUSE_TYPE = (
    (PG,'PG'),  #
    (HOUSE,'HOUSE'),
    (VILLA,'VILLA'),
    (FLAT,'FLAT'),
)

SHARED  = 'SHARED'
PRIVATE = 'PRIVATE'

ACCOM_TYPE = (
    (SHARED,'SHARED'),
    (PRIVATE,'PRIVATE'),
)


class  Post(Address,object):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    title = models.CharField(max_length=100)
    description  = models.CharField(max_length=40)
    rentperday  = models.IntegerField(default=0,blank=True)
    deposit     = models.IntegerField(default=0,blank=True)
    guests   = models.IntegerField(default=0,blank=True)

    house_type =  models.CharField(max_length=10,choices=HOUSE_TYPE,default=PG)
    accom_type = models.CharField(max_length=10,choices=ACCOM_TYPE,default=PRIVATE)
    accom_for = models.CharField(max_length=20,blank=True)

    facilities = models.CharField(max_length=255,blank=True)

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


class  PostPhoto(models.Model):
    photo = models.ImageField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='postphotos')
    class Meta:
        ordering = ('id',)
        db_table = "images"


class  ShortlistedPosts(Address,object):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='bookmarks')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    class Meta:
        ordering = ('id',)
        db_table = "post_shortlistings"

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

