from django.urls import path

from usefulthings.apps import UsefulthingsConfig
from usefulthings.views import (
    PublishedWontListView,
    WontCreateApiView,
    WontDestroyApiView,
    WontListApiView,
    WontRetrieveApiView,
    WontUpdateApiView,
)

app_name = UsefulthingsConfig.name

urlpatterns = [
    path("wont/create/", WontCreateApiView.as_view(), name="wont-create"),
    path("wont/", WontListApiView.as_view(), name="wont-list"),
    path("wont/<int:pk>/", WontRetrieveApiView.as_view(), name="wont-retrieve"),
    path("wont/<int:pk>/update/", WontUpdateApiView.as_view(), name="wont-update"),
    path("wont/<int:pk>/delete/", WontDestroyApiView.as_view(), name="wont-delete"),
    path(
        "published-wont/", PublishedWontListView.as_view(), name="published-wont-list"
    ),
]
