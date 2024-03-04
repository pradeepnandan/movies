from django.db import models

# Create your models here.
class movies(models.Model):
    mname=models.CharField(max_length=250)
    desc=models.TextField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.mname