from datetime import date

from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import News, SavedArticle
from . import models
from . import serializers
from rest_framework import viewsets, permissions


class NewsViewSet(viewsets.ModelViewSet):
    """ViewSet for the News class"""

    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer

    # permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        queryset = News.objects.all()

    @action(detail=False)
    def categories(self, request):
        news = News.objects.order_by().values('category').distinct()
        serializer = serializers.CategoriesSerializer(news, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = News.objects.filter()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(Q(category=category)).exclude(video=None)
        if category == "videos":
            queryset = queryset.exclude(video=None)
        serializer = serializers.NewsSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def save(self, request, *args, **kwargs):
        SavedArticle(user=request.user, news=kwargs["pk"]).save()

    @action(detail=True)
    def remove(self, request, *args, **kwargs):
        SavedArticle(user=request.user, news=kwargs["pk"]).delete()

    @action(detail=False)
    def saved(self, request, *args, **kwargs):
        queryset = SavedArticle.objects.filter(user=request.user)
        serializer = serializers.SavedArticleSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the News class"""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoriesSerializer
