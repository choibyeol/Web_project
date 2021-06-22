from django.urls import path, include
from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'calendar_board'

urlpatterns = [
    url(r'^$', views.calendar_board.as_view(), name='calendar_board'),
    url(r'^insert/$', views.check_post, name='calendar_board_insert'),
    url(r'^save_prioirity/$', views.check_post, name='calendar_board_save_priority'),
    url(r'^is_complete/$', views.check_post, name='calendar_board_is_complete'),
    url(r'^is_non_complete/$', views.check_post, name='calendar_board_is_non_complete'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.calendar_board_detail.as_view(), name='calendar_board_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.calendar_board_update.as_view(), name='calendar_board_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.calendar_board_delete.as_view(), name='calendar_board_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
