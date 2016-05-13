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



PROGRESS='progress'
PENDING ='pending'
VERIFIED='verified'
REJECTED='Rejected'

POST_STATE = (
    (PROGRESS,'progress'),
    (PENDING,'pending'),  #
    (VERIFIED,'verified'),
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
class User(Address):
    emailid = models.EmailField(max_length=30,db_index=True,unique=True)    
    password = models.CharField(max_length=15,blank=True)
    phone_number = models.CharField(max_length=10,db_index=True,unique=True)
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

    class Meta:
        ordering = ('id',)

@python_2_unicode_compatible
class  Post(Address):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    description  = models.CharField(max_length=40,blank=True)
    rentperday  = models.IntegerField(blank=True,default=10)
    keywords = models.CharField(max_length=50,blank=True)
    facilities = models.CharField(max_length=50,blank=True)
    avail_start_date = models.DateField(blank=True,null=True)
    avail_end_date = models.DateField(blank=True,null=True)
    status  =  models.CharField(max_length=1,blank=True,choices=POST_STATE,default=PROGRESS)
    is_active = models.CharField(max_length=1,blank=True,choices=STATUS,default=NO)

    created = models.DateTimeField(auto_now_add=True,blank=True)
    last_modified = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.description
