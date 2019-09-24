
from django.urls import path
import .views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:product_id>/", views.product_info)
]
