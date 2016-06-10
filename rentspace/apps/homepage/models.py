from django.db import models


MALE = 'M'
FEMALE = 'F'
GENDER = (
    (MALE,'Male'),
    (FEMALE,'Female'),
)

TRUE = 'T'
FALSE = 'F'

YES  = 'Y'
NO ='N'

STATUS = (
    (YES,'Yes'),
    (NO,'No'),
)

PENDING ='PENDING'
ACCEPTED='ACCEPTED'
REJECTED='REJECTED'

STATE = (
    (PENDING,'PENDING'),  #
    (ACCEPTED,'ACCEPTED'),
    (REJECTED,'REJECTED'),
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
        db_table="address"

class Date(models.Model):
    day = models.IntegerField(blank=True)
    month = models.IntegerField(blank=True)
    year  = models.IntegerField(blank=True)
    class Meta:
        abstract = True
        db_table = "dmy"

