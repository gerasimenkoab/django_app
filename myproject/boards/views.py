from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Board


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