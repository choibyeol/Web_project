from django.shortcuts import render
from .models import BoardList

from django.views import View
from django.views import generic

class calendar_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'calendar_board/board_list.html'
        board_list = BoardList.objects.all()
        return render(request, template_name, {"board_list": board_list})
