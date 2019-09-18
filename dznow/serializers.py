from . import models

from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ('__all__')


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('__all__')


class SavedArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SavedArticle
        field = ("__all__")
