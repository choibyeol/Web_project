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

class calendar_board_update(generic.UpdateView):
    model = BoardList
    fields = ('title', 'content', 'end_date')
    template_name = 'calendar_board/calendar_board_update.html'
    success_url = '/board/'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'calendar_board/calendar_board_success.html', {"message": "일정을 업데이트 했습니다."})

    def get(self, request, *args, **kwargs):
        # 오브젝트를 받아와서 폼 클래스를 받아온 후 이것을 return
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

class calendar_board_delete(generic.DeleteView):
    model = BoardList
    success_url = '/board/'
    context_object_name = 'board_list'

def check_post(request):
    template_name = 'calendar_board/calendar_board_success.html'
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.board_save()
            message = "일정을 추가했습니다."
            return render(request, template_name, {"message": message})
    else:
        template_name = 'calendar_board/calendar_board_insert.html'
        form = BoardForm
        return render(request, template_name, {"form": form})
