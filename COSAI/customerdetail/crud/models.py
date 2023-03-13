
from django.db import models 
from django.core.files.storage import FileSystemStorage 
class Uploadedfiles(models.Model):  
    uploads1=models.FileField(upload_to='uploads/',null=True)
class Meta:          
        db_table = "customer"