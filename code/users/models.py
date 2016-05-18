from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

'''
emailid    
password
phone no
firstname
lastname

adddress
id_card_type
id_card(bytes)
is_email_verified
is_phone_verified
is_id_verified

createdon
updatedon
is_phone_verified
is_email_verified
is_idcard_verified

DOB day,month,year
'''

MALE = 'M'
FEMALE = 'F'
GENDER = (
    (MALE,'Male'),
    (FEMALE,'Female'),
)

TRUE = 'T'
YES  = 'T'
FALSE = 'F'
NO ='F'

STATUS = (
    (YES,'Yes'),
    (NO,'No'),
)



PENDING ='P'
ACCEPTED='A'
REJECTED='R'

POST_STATE = (
    (PENDING,'pending'),  #
    (ACCEPTED,'accepted'),
    (REJECTED,'rejected'),
)


class Address(models.Model):
    address1 = models.CharField(max_length=20,blank=True)
    address2 = models.CharField(max_length=20,blank=True)
    street   = models.CharField(max_length=20,blank=True)
    city     = models.CharField(max_length=20,blank=True)
    state    = models.CharField(max_length=20,blank=True)
    country  = models.CharField(max_length=20,blank=True)
    zipcode  = models.CharField(max_length=20,blank=True)
    google_map = models.CharField(max_length=20,blank=True)

    class Meta:
        abstract = True

class Date(models.Model):
    day = models.IntegerField(blank=True)
    month = models.IntegerField(blank=True)
    year  = models.IntegerField(blank=True)
    class Meta:
        abstract = True



@python_2_unicode_compatible
class User(Address,object):
    emailid = models.EmailField(max_length=30,db_index=True,unique=True)    
    password = models.CharField(max_length=15,blank=True)
    phone_number = models.CharField(max_length=10,blank=True,db_index=True,unique=True)
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)

    date_of_birth = models.DateField(blank=True,null=True)
    id_card_type = models.CharField(max_length=20,blank=True)
    id_card_data = models.CharField(max_length=20,blank=True)
    is_email_verified = models.CharField(max_length=1,blank=True,choices=STATUS,default=NO)
    is_phone_verified = models.CharField(max_length=1,blank=True,choices=STATUS,default=NO)
    is_id_verified =models.CharField(max_length=1,blank=True,choices=STATUS,default=NO)

    gender = models.CharField(max_length=2,blank=True,choices=GENDER,default=MALE)    
    created = models.DateTimeField(auto_now_add=True,blank=True)
    last_modified = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.emailid
    
    def __setitem__(self, key, value):
        object.__setattr__(self, key, value)

    class Meta:
        ordering = ('id',)

@python_2_unicode_compatible
class  Post(Address,object):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    description  = models.CharField(max_length=40,blank=True)
    rentperday  = models.IntegerField(blank=True,default=10)
    facilities = models.CharField(max_length=50,blank=True)
    avail_start_date = models.DateField(blank=True,null=True)
    avail_end_date = models.DateField(blank=True,null=True)
    status  =  models.CharField(max_length=1,blank=True,choices=POST_STATE,default=PENDING)
    is_active = models.CharField(max_length=1,blank=True,choices=STATUS,default=NO)
    is_verified = models.CharField(max_length=1,blank=True,choices=STATUS,default=NO)
    keywords = models.CharField(max_length=50,blank=True)

    created = models.DateTimeField(auto_now_add=True,blank=True)
    last_modified = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.description

    def __setitem__(self, key, value):
        object.__setattr__(self, key, value)

class PostAttributes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='attributes')
    name = models.CharField(max_length=40,blank=True)
    value = models.CharField(max_length=40,blank=True)

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='photos')
    title = models.CharField(max_length=25,blank=True)
    description = models.CharField(max_length=50,blank=True)
    filepath = models.CharField(max_length=50,blank=True)   
    filetype = models.CharField(max_length=10,blank=True)
    size = models.IntegerField(blank=True,default=0)
    status  = models.CharField(max_length=1,blank=True,choices=POST_STATE,default=PENDING)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    reviewedby = models.ForeignKey(User, null=True, on_delete=models.CASCADE,related_name='comments')
    username  = models.CharField(max_length=50,blank=True)
    description = models.CharField(max_length=100,blank=True)
    status = models.CharField(max_length=1,blank=True,choices=POST_STATE,default=PENDING)



