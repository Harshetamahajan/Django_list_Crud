from django.db import models
from django.forms import FilePathField

# Create your models here.
class User(models.Model):
    user_id= models.AutoField
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    number=models.IntegerField(null=True, blank=True)
    image= models.ImageField(upload_to= "image",null=True,blank=True )
 
    def return_profile_picture(self):
    
        if self.image:
            return f"http://127.0.0.1:8005/static/images/{self.image}"
        return None
  