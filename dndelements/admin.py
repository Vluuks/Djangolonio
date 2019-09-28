from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Player)
admin.site.register(Campaign)
admin.site.register(NPC)
admin.site.register(Race)
admin.site.register(PlayerClass)
admin.site.register(Item)
admin.site.register(StatList)
