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
    news = NewsSerializer()

    class Meta:
        depth = 1
        model = models.SavedArticle
        fields = ("news",)
