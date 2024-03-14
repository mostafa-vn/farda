from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("newfardaapp.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("newfardaapp.urls")),
]