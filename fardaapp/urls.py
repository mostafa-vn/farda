from django.urls import include, path

from fardaapp.views import UserInfo

urlpatterns = [
    path("register", UserInfo.as_view(), name="user-register")
]