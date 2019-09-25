from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

from .models import Board, Topic, Post
from .forms import NewTopicForm

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

def create_topic_view(request, board_id):

    try:
        board = Board.objects.get(pk=board_id)
    except Board.DoesNotExist:
        raise Http404("Board does not exist")

    # check whether user is logged in 
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})

    user = request.user

    if(request.method == 'POST'):
        form = NewTopicForm(request.POST)
        
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )

            # can contain the name of the url, then also the required arguments 
            return redirect('board_topics', board_id=board.pk)

    elif(request.method == 'GET'):
        form = NewTopicForm()

    return render(request, 'forum/new_topic.html', {'board': board, 'form': form})