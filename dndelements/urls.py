from django.urls import path
from . import views

urlpatterns = [
    path("campaigns/", views.campaigns, name="dnd_campaigns"),
    path("campaigns/<int:campaign_id>/", views.campaign_details, name="dnd_campaign_details"),

    path("characters/", views.characters, name="dnd_characters"),
    path("characters/<int:character_id>/", views.character_details, name="dnd_character_details"),
    
    path("npcs/", views.npcs, name="dnd_npcs"),
    path("monsters/", views.monsters, name="dnd_monsters"),
    path("items/", views.items, name="dnd_items"),
    path("locations/", views.locations, name="dnd_locations")
]