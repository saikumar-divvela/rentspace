from django.db import models

# Create your models here.

'''
class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='photos')
    title = models.CharField(max_length=25,blank=True)
    description = models.CharField(max_length=50,blank=True)
    url = models.CharField(max_length=50,blank=True)   
    filename = models.CharField(max_length=50,blank=True)
    filepath = models.CharField(max_length=100,blank=True)      
    filetype = models.CharField(max_length=10,blank=True)
    size = models.IntegerField(blank=True,default=0)
    status  = models.CharField(max_length=10,blank=True,choices=STATE,default=PENDING)

    @property
    def filedata(self):
        return "test file data"
    
    class Meta:
        ordering = ('id',)
        db_table = "media"
'''
