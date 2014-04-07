from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import Poll


def index(request):
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #context = {'latest_poll_list': latest_poll_list}
    #return render(request, 'polls/index.html', context)
    return HttpResponse("This is the board list")


def board(request, board_id):
    return HttpResponse("This is the topic list for board {}.".format(board_id))


def topic(request, topic_id):
    return HttpResponse("This is the message list for topic {}.".format(topic_id))


def message(request, message_id):
    return HttpResponse("Message detail for message {}.".format(message_id))




# Create your views here.
