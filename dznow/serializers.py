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


class SavedArticleListSerializer(serializers.ModelSerializer):
    # news = NewsSerializer()
    id = serializers.ReadOnlyField(source="news.id")
    title = serializers.ReadOnlyField(source="news.title")
    content = serializers.ReadOnlyField(source="news.content")
    resume = serializers.ReadOnlyField(source="news.resume")
    author = serializers.ReadOnlyField(source="news.author")
    link = serializers.ReadOnlyField(source="news.link")
    video = serializers.ReadOnlyField(source="news.video")
    category = serializers.ReadOnlyField(source="news.category.name")
    source = serializers.ReadOnlyField(source="news.source")
    date = serializers.ReadOnlyField(source="news.date")
    image = serializers.ReadOnlyField(source="news.image")

    class Meta:
        depth = 0
        model = models.SavedArticle
        fields = ("id", "title", "content", "resume", "author", "link", "video",
                  "source", "date", "category", "image")


class SavedArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SavedArticle
        fields = ("__all__")
