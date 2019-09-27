from django.urls import include, path

urlpatters = [
    path("", views.index, name="index")
]