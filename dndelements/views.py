from django.shortcuts import render

# Viewing existing elements
def campaigns(request):
    return render(request, 'dndelements/campaigns.html')

def characters(request):
    return render(request, 'dndelements/characters.html')

def npcs(request):
    return render(request, 'dndelements/npcs.html')

def monsters(request):
    return render(request, 'dndelements/monsters.html')

def items(request):
    return render(request, 'dndelements/items.html')

def locations(request):
    return render(request, 'dndelements/locations.html')

