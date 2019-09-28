from django.shortcuts import render
from django.http import Http404
from .models import *
from django.core import serializers
from .helpers import calculate_modifier


# Viewing existing elements
def campaigns(request):

    context = {
        "name" : "Campaigns",
        "data" : Campaign.objects.all()
    }

    return render(request, 'dndelements/campaigns.html', context)

def campaign_details(request, campaign_id):

    try:
        campaign = Campaign.objects.get(pk=campaign_id)
    except Campaign.DoesNotExist:
        raise Http404("Campaign does not exist")
    
    context = {
        "campaign" : campaign
    }
    return render(request, "dndelements/campaign_details.html", context)

def characters(request):
    
    context = {
        "name" : "Characters",
        "data" : Player.objects.all()
    }
    return render(request, 'dndelements/characters.html', context)


def character_details(request, character_id):
    try:
        character = Player.objects.get(pk=character_id)
    except Player.DoesNotExist:
        raise Http404("Character does not exist")


    
    # calculate modifiers
    stats_dict = {}

    print("KIJK HIER JONGE")
    serialized = serializers.serialize("python", [character.player_stats])
    print(serialized)
    print("------------------")
    print(serialized[0]['fields'])
    
    for i, (field, value) in enumerate(serialized[0]['fields'].items()):
        stats_dict[field] = [value, calculate_modifier(value)]
    
    print(stats_dict)
    
    context = {
        "character" : character,
        "statlist" : serializers.serialize("python", [character.player_stats] ),
        "statlist_modifiers" : stats_dict
    }
    return render(request, "dndelements/character_details.html", context)







def npcs(request):
    return render(request, 'dndelements/npcs.html')

def monsters(request):
    return render(request, 'dndelements/monsters.html')

def items(request):
    return render(request, 'dndelements/items.html')

def locations(request):
    return render(request, 'dndelements/locations.html')

