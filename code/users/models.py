from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

'''
emailid
firstname
lastname
phone no
createdon
updatedon
is_phone_verified
is_email_verified
is_idcard_verified
'''

@python_2_unicode_compatible
class User(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER = (
        (MALE,'Male'),
        (FEMALE,'Female'),
    )
    
    emailid = models.EmailField(max_length=30,db_index=True,unique=True)    
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=30,blank=True)
    password = models.CharField(max_length=15,blank=True)
    phone_number = models.CharField(max_length=10,db_index=True,unique=True)
    gender = models.CharField(max_length=2,blank=True,choices=GENDER,default=MALE)    
    created = models.DateTimeField(auto_now_add=True,blank=True)
    last_modified = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.emailid

    class Meta:
        ordering = ('id',)