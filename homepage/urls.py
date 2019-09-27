from django.urls import include, path
from . import views

urlpatters = [
    path("", views.index, name="index")
]