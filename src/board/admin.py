from django.contrib import admin
from board.models import Board, Topic, Message


"""class ChoiceInline(admin.TabularInline):

    model = Choice
    extra = 3
"""


class BoardAdmin(admin.ModelAdmin):
    fields = ['title', 'description']

admin.site.register(Board, BoardAdmin)


class TopicAdmin(admin.ModelAdmin):
    fields = ['title', 'board']

admin.site.register(Topic, TopicAdmin)


class MessageAdmin(admin.ModelAdmin):
    fields = ['post_time', 'text', 'user']

admin.site.register(Message, MessageAdmin)

