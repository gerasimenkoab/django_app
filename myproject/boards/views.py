from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post
from django.contrib.auth.models import User


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
    return HttpResponse("Creator mada dis")

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

        return render(request, 'topics.html', {'board': board})
        #return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page

    return render(request, 'new_topic.html', {'board': board})