from django.contrib import admin

# Register your models here.
from .models import Player, Campaign, NPC, Race

admin.site.register(Player)
admin.site.register(Campaign)
admin.site.register(NPC)
admin.site.register(Race)