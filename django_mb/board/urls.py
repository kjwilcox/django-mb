from django.conf.urls import patterns, url

from board import views

urlpatterns = patterns('',
    # ex: /mb/
    url(r'^$', views.index, name='index'),

    # ex: /mb/board/5/
    url(r'^board/(?P<board_id>\d+)/$', views.board, name='board'),

    # ex: /mb/topic/17/
    url(r'^topic/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # ex: /mb/message/17/
    url(r'^message/(?P<message_id>\d+)/$', views.message, name='message'),

)
