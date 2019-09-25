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

    # get user
    # user = request.user

    user = "Someone"

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
            return redirect('forum/topics', pk=board.pk)

    elif(request.method == 'GET'):
        form = NewTopicForm()

    return render(request, 'forum/new_topic.html', {'board': board, 'form': form})