from django.db import models

# Create your models here.
class tunis(models.Model):
    name=models.CharField(max_length=500)
    age=models.IntegerField()
    etude=models.BooleanField(default=False)
    
    
    
    
    



    def __str__(self):
        return self.name
 
  

   
