from django.shortcuts import render
from django.http import HttpResponse

from .models import Board

def index(request):
    return HttpResponse("TEST!!")

# Create your views here.
def home_view(request):
    boards = Board.objects.all()
    return render(request, 'forum/home.html', {'boards': boards})