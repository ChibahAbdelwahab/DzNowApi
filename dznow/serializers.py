from . import models

from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ('__all__')


class CategoriesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = models.News 
        fields = ('category', "image")
