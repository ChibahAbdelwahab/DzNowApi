# Create your models here.
from django.db import models


class Category(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100, primary_key=True)


class News(models.Model):
    title = models.CharField(max_length=100)
    resume = models.TextField()
    content = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    image = models.ImageField()
    source = models.CharField(max_length=50)
    link = models.URLField()
    video = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        unique_together = ('date', 'title', 'source')
        ordering = ('date',)
