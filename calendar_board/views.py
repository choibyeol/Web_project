from django.shortcuts import render, redirect
from .models import BoardList
from .forms import BoardForm

from django.views import View
from django.views import generic

class calendar_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'calendar_board/calendar_board_list.html'
        board_list = BoardList.objects.all()
        return render(request, template_name, {"board_list": board_list})

class calendar_board_detail(generic.DetailView):
    model = BoardList
    template_name = 'calendar_board/calendar_board_detail.html'
    context_object_name = 'board_list'

def check_post(request):
    template_name = 'calendar_board/calendar_board_success.html'
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.board_save()
            message = "일정을 추가하였습니다."
            return render(request, template_name, {"message": message})
    else:
        template_name = 'calendar_board/calendar_board_insert.html'
        form = BoardForm
        return render(request, template_name, {"form": form})
