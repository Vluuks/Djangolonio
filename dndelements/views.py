from django.shortcuts import render, redirect
from django.http import Http404
from .models import *
from django.core import serializers
from .helpers import calculate_modifier
from .forms import NewNPCForm
import logging
import json


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
    serialized = serializers.serialize("python", [character.player_stats])

    for i, (field, value) in enumerate(serialized[0]['fields'].items()):
        stats_dict[field] = [value, calculate_modifier(value)]
  
    context = {
        "character" : character,
        "statlist" : serializers.serialize("python", [character.player_stats] ),
        "statlist_modifiers" : stats_dict
    }
    return render(request, "dndelements/character_details.html", context)



def npcs(request):

    context = {
        "name" : "NPCs",
        "data" : NPC.objects.all(),
        "npcs_json" :  serializers.serialize('json', NPC.objects.all())
    }
    return render(request, 'dndelements/npcs.html', context)

def npcs_new(request):

    if(request.method == 'POST'):
        form = NewNPCForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data["name"]
            alignment = form.cleaned_data["alignment"]
            race = form.cleaned_data["race"]
            status = form.cleaned_data["status"]
            gender = form.cleaned_data["gender"]
            age = form.cleaned_data["age"]

            logging.debug(race)

            npc = NPC(
                name=name,
                alignment=alignment,
                race=race,
                status=status,
                gender=gender,
                age=age
            )
            npc.save()

            return redirect('dnd_npcs')

    form = NewNPCForm()
    context = { 'form': form }

    return render(request, 'dndelements/add_npc.html', context)

def npc_details(request, npc_id):

    try:
        npc = NPC.objects.get(pk=npc_id)
    except NPC.DoesNotExist:
        raise Http404("NPC does not exist")

    context = {
        "npc" : npc
    }
    return render(request, 'dndelements/npc_details.html')







def monsters(request):
    return render(request, 'dndelements/monsters.html')

def items(request):
    return render(request, 'dndelements/items.html')

def locations(request):
    return render(request, 'dndelements/locations.html')

