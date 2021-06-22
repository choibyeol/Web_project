from django.urls import path, include
from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'calendar_board'

urlpatterns = [
    url(r'^$', views.calendar_board.as_view(), name='calendar_board'),
    url(r'^insert/$', views.check_post, name='calendar_board_insert'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
