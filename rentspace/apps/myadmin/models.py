from django.db import models

# Create your models here.
class  Postbox(models.Model):
    name    = models.CharField(max_length=50)
    email   = models.EmailField(max_length=50,db_index=True)
    phone_number   = models.CharField(max_length=10,db_index=True)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    sent_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="postbox"