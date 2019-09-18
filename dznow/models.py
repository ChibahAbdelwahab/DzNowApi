# Create your models here.
from argparse import _

from django.db import models
from rest_framework.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from fcm_django.fcm import fcm_send_topic_message
from django.contrib.auth.models import User


class Category(models.Model):
    image = models.CharField(max_length=1000)
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


# Notify users in FCM
@receiver(post_save, sender=News, dispatch_uid="notify_users_fcm")
def notify_users(sender, instance, **kwargs):
    title = instance.title[:30] + ".." if len(
        instance.title) > 30 else instance.title
    resume = instance.resume[:40] + ".." if len(
        instance.resume) > 40 else instance.resume
    fcm_send_topic_message(topic_name=instance.category.name,
                           message_body=resume,
                           message_title=title)


class SavedArticle(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE,default=1)
    iduser = models.CharField(max_length=1000, default="1")
