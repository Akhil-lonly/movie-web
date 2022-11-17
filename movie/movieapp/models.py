from django.db import models

# Create your models here.
class movie(models.Model):
    Name=models.CharField(max_length=150)
    desc=models.TextField()
    year=models.IntegerField()
    Image=models.ImageField(upload_to='gallery')
    def __str__(self):
        return self.Name


