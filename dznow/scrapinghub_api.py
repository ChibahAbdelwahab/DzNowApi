from datetime import datetime

import requests
from django.utils.timezone import make_aware

from .models import *

API_KEY = "be9b53f6ff094d3f8d37c8b63bb1fcd8"
PROJECT_ID = "406520"


# client = ScrapinghubClient(API_KEY)
# project = client.get_project(PROJECT_ID)
#
#
# def run_jobs():
#     for ii in project.spiders.list():
#         try:
#             spider = project.spiders.get(ii)
#             spider.jobs.run()
#         except Exception as e:
#             print(e)


def get_jobs():
    url = "https://storage.scrapinghub.com/jobq/" + PROJECT_ID + \
          "/list?format=json&apikey=" + API_KEY + "&state=finished&count=10"
    r = requests.get(url)
    return r.json()


def update():
    for data in get_jobs():
        id = data["key"]
        url = "https://storage.scrapinghub.com/items/" + str(
            id) + "?format=json&sep=;&apikey=" + API_KEY
        r = requests.get(url)
        for i in r.json():
            i.pop("_type")
            try:
                print(i["category"])
                i["date"] = make_aware(
                    datetime.fromtimestamp(i["date"] / 1000)).strftime(
                    "%Y-%m-%d %H:%M:%S")
                i["category"] = i["category"].lower().capitalize()
                if i["category"][-1:] == "s":
                    i["category"] = i["category"][:-1]
                category = Category.objects.get(name=i["category"])
                if category is None:
                    Category.objects.get(name="Divers")
                i["category"] = category
                News.objects.create(**i)
            except Exception as e:
                print(e)
