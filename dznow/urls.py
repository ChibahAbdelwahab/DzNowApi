from django.http import HttpResponse
from django.urls import path, include
from rest_framework import routers
import requests

from .scrapinghub_api import update
from . import api

router = routers.DefaultRouter()
router.register(r'news', api.NewsViewSet)


def perform_save(request):
    print("saving")
    update()
    return HttpResponse('Updated', status=200)

urlpatterns = (
    # urls for Django Rest Framework API
    path('update', perform_save),
    path('', include(router.urls)),
)
