from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home_view, name="home"),
    path("boards/<int:board_id>/", views.board_view, name="board")
]
