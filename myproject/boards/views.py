from django.shortcuts import render
#from django.http import HttpResponse
from .models import Board

# Create your views here.
def home(request):
    """View  with a simple response."""
    boards = Board.objects.all()
    # board_names = list()
    # for board in boards:
    #     board_names.append(board.name)

    # responseHTML = '<br>'.join(board_names)

    # return HttpResponse(responseHTML)
    return render(request, 'home.html',{'boards':boards})