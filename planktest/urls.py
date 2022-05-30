from django.contrib import admin
from django.urls import path
from satellites.views import satellites_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", satellites_api.urls),
]
