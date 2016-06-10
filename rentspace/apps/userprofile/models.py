from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from homepage.models import *

# Create your models here.

'''
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10,blank=True,db_index=True,unique=True)


    class Meta:
        ordering = ('id',)
        db_table = "userprofile"

'''
class MyUserManager(BaseUserManager):
    def create_user(self, email,password,phone_number):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.phone_number = phone_number
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,phone_number):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,password=password,phone_number=phone_number)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,Address):


    email = models.EmailField(max_length=50,verbose_name='email address',db_index=True,unique=True)    
    first_name = models.CharField(max_length=40,blank=True)
    last_name = models.CharField(max_length=40,blank=True)
    phone_number = models.CharField(max_length=10,blank=True,db_index=True,unique=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    date_of_birth = models.DateField(null=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)


    id_card_type = models.CharField(max_length=20,blank=True)
    id_card_data = models.CharField(max_length=20,blank=True)

    is_email_verified = models.CharField(max_length=1,choices=STATUS,default=NO)
    is_phone_verified = models.CharField(max_length=1,choices=STATUS,default=NO)
    is_id_verified =models.CharField(max_length=1,choices=STATUS,default=NO)
    gender = models.CharField(max_length=1,blank=True,choices=GENDER,default=MALE)    

    objects = MyUserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[phone_number]


    class Meta:
        ordering = ('id',)
        db_table = "user"

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name+" "+self.last_name    

    def get_short_name(self):
        return self.first_name

    def __str__(self):   
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin