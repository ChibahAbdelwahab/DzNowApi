# Create your models here.
from django.db import models
from rest_framework.exceptions import ValidationError


class Category(models.Model):
    image = models.URLField()
    name = models.CharField(max_length=100, primary_key=True)


class News(models.Model):
    title = models.CharField(max_length=100)
    resume = models.TextField(null=False)
    content = models.TextField(null=False)
    date = models.DateTimeField(null=False)
    author = models.CharField(max_length=100, null=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,
                                 null=False)
    image = models.URLField(null=False)
    source = models.CharField(max_length=50, null=False)
    link = models.URLField(null=False, )
    video = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '%s %s %s ' % (self.title, self.category.name, self.source)

    class Meta:
        unique_together = ('date', 'title', 'source')
        ordering = ('-date',)

    def clean(self):
        if self.category.name == "videos" and self.video is None:
            raise ValidationError(
                _('Video must not be null for video category'))
