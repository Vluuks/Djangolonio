from django.shortcuts import render
from .pagelist import entries

# Create your views here.
def index(request):
    return render(request, "homepage/index.html", { "pages" : entries })
