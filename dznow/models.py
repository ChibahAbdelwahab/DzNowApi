# Create your models here.
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    resume = models.TextField()
    content = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.ImageField()
    source = models.CharField(max_length=50)
    link = models.URLField()
    video = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = ('date', 'title', 'source')
