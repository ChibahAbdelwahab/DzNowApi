from django.http import HttpResponse
from django.urls import path, include
from rest_framework import routers
import requests

from .scrapinghub_api import update
from . import api

router = routers.DefaultRouter()
router.register(r'news', api.NewsViewSet)
router.register(r'category', api.CategoryViewSet)


def perform_save(request):
    print("saving")
    update()
    return HttpResponse('Updated', status=200)


def notify():
    # Send to single device.
    from pyfcm import FCMNotification

    push_service = FCMNotification(api_key="<api-key>")

    # Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

    registration_id = "<device registration_id>"
    message_title = "Uber update"
    message_body = "Hi john, your customized news for today is ready"
    result = push_service.notify_single_device(registration_id=registration_id,
                                               message_title=message_title,
                                               message_body=message_body)

    # Send to multiple devices by passing a list of ids.
    registration_ids = ["<device registration_id 1>",
                        "<device registration_id 2>", ...]
    message_title = "Uber update"
    message_body = "Hope you're having fun this weekend, don't forget to check today's news"
    result = push_service.notify_multiple_devices(
        registration_ids=registration_ids, message_title=message_title,
        message_body=message_body)

    print(result)


urlpatterns = (
    # urls for Django Rest Framework API
    path('update', perform_save),
    path('', include(router.urls)),
)
