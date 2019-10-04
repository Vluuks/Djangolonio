from django.urls import path
from . import views

urlpatterns = [

    # campaigns
    path("campaigns/", views.campaigns, name="dnd_campaigns"),
    path("campaigns/<int:campaign_id>/", views.campaign_details, name="dnd_campaign_details"),

    # player characters
    path("characters/", views.characters, name="dnd_characters"),
    path("characters/<int:character_id>/", views.character_details, name="dnd_character_details"),
    path("characters/new/", views.character_new, name="dnd_character_new"),
    
    # dm characters
    path("npcs/", views.npcs, name="dnd_npcs"),
    path("npcs/<int:npc_id>/", views.npc_details, name="dnd_npc_details"),
    path("npcs/new/", views.npcs_new, name="dnd_npc_new"),

    # monsters/enemies
    path("monsters/", views.monsters, name="dnd_monsters"),

    # items such as consumables and weapons
    path("items/", views.items, name="dnd_items"),


    path("locations/", views.locations, name="dnd_locations")
]