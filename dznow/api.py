from datetime import date

from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import News
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
            queryset = queryset.filter(Q(category=category))
        serializer = serializers.NewsSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for the News class"""

    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoriesSerializer
