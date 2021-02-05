from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300,default="default title")
    date = models.DateTimeField(null=True)
    text = models.TextField()
    image = models.ImageField(upload_to='event_images/')

