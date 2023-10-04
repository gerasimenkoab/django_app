from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm


# Create your views here.
def home(request):
    """View  with a simple response."""
    boards = Board.objects.all()
    return render(request, 'home.html',{'boards':boards})

def board_topics(request, pk=1):
    try:
        board = Board.objects.get(pk = pk) #pk ----- primary key
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})

def about(request):
    return render(request,'about.html')
    #return HttpResponse("Creator mada dis")

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first() # TODO: get current user 
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit = False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                topic = topic,
                created_by = user
            )
            return redirect('board_topics',pk = board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html',{'board':board,'form':form})
