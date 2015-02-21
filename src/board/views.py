from django.shortcuts import render
from django.http import HttpResponse

from board.models import Board, Topic, Message


def index(request):
    board_list = Board.objects.all()
    context = {'board_list': board_list}
    return render(request, 'board/index.html', context)


def board(request, board_id):
    topic_list = Topic.objects.filter(board=board_id)
    context = {'topic_list': topic_list}
    return render(request, 'board/board.html', context)


def topic(request, topic_id):
    message_list = Message.objects.filter(topic=topic_id)
    context = {'message_list': message_list}
    return render(request, 'board/topic.html', context)


def message(request, message_id):
    return HttpResponse("Message detail for message {}.".format(message_id))




# Create your views here.
