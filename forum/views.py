from django.shortcuts import render
from django.http import HttpResponse

from .models import Board

def index(request):
    return HttpResponse("TEST!!")

# Create your views here.
def home_view(request):
    boards = Board.objects.all()
    return render(request, 'forum/home.html', {'boards': boards})

def board_view(request, board_id):

    try:
        board = Board.objects.get(pk=board_id)
    except Board.DoesNotExist:
        raise Http404("Board does not exist")
    
    context = {
        "board" : board
    }
    return render(request, "forum/topics.html", context)