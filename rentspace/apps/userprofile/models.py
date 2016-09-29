from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from rest_framework.authtoken.models import Token
from django.conf import settings

from homepage.models import *

"""
Ceates and saves a User with the given email, date of birth and password.
"""
class MyUserManager(BaseUserManager):
    def create_user(self, email,password,phone_number):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.phone_number = phone_number
        user.set_password(password)
        user.save(using=self._db)
        return user

    """
        Creates and saves a superuser with the given email, date of birth and password.
    """
    def create_superuser(self, email, password,phone_number):
        user = self.create_user(email,password=password,phone_number=phone_number)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,Address):
    email = models.EmailField(max_length=50,verbose_name='email address',db_index=True,unique=True)
    first_name = models.CharField(max_length=40,blank=True)
    last_name = models.CharField(max_length=40,blank=True)
    phone_number = models.CharField(max_length=10,blank=True,db_index=True,unique=True)
    gender = models.CharField(max_length=1,blank=True,choices=GENDER,default=MALE)
    date_of_birth = models.DateField(null=True)

    id_card_type = models.CharField(max_length=20,blank=True)
    idphoto = models.ImageField(blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login_date = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)

    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    is_id_verified = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)



    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [phone_number]


    class Meta:
        ordering = ('id',)
        db_table = "user"

    def get_full_name(self):
        return self.first_name+" "+self.last_name

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    """Does the user have a specific permission? # Simplest possible answer: Yes, always"""
    def has_perm(self, perm, obj=None):
        return True

    """Does the user have permissions to view the app `app_label`? # Simplest possible answer: Yes, always"""
    def has_module_perms(self, app_label):
        return True

    def __setitem__(self, key, value):
        object.__setattr__(self, key, value)

class UserKey(models.Model):
    user = models.OneToOneField(User, related_name='profile') #1 to 1 link with Django User
    activation_key = models.CharField(max_length=40)
    key_expires = models.DateTimeField()
    class Meta:
        ordering = ('id',)
        db_table = "userkey"

'''
from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


for user in User.objects.all():
    Token.objects.get_or_create(user=user)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10,blank=True,db_index=True,unique=True)


    class Meta:
        ordering = ('id',)
        db_table = "userprofile"

'''
